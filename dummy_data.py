import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
import csv
import random
import itertools
from faker import Faker
from django.core.files import File
from taggit.models import Tag
from django.utils.text import slugify
from django.conf import settings
from products.models import Category, BrandCategory, Brand, CategorySuggest, FlagOption, Product, ProductImage

fake = Faker()

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(script_dir, 'csv')

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def seed_category(num_rows=None):
    category_file = os.path.join(csv_dir, 'dummy_category.csv')
    category_data = read_csv_file(category_file)
    if num_rows is not None:
        category_data = category_data[:num_rows]
        
    categories = []
    for row in category_data:
        image_filename = row['image_filename']
        dummy_data_name = row['dummy_data_name']
        if image_filename is None:
            continue
        image_path = os.path.join(settings.STATIC_ROOT, 'images', 'category', image_filename)

        with open(image_path, 'rb') as f:
            category = Category.objects.create(
                name=dummy_data_name,
                image=File(f, name=image_filename)
            )
            categories.append(category)
        print(f'Successfully created Category: {category.name}, Image Filename: {image_filename}')

    return categories

def seed_suggest(num_rows=None):
    suggest_file = os.path.join(csv_dir, 'dummy_suggest.csv')
    suggest_data = read_csv_file(suggest_file)
    if num_rows is not None:
        suggest_data = suggest_data[:num_rows]

    for row in suggest_data:
        image_filename = row['image_filename']
        dummy_data_name = row['dummy_data_name']
        image_path = os.path.join(settings.STATIC_ROOT, 'images', 'suggest', image_filename)

        with open(image_path, 'rb') as f:
            suggest = CategorySuggest.objects.create(
                name=dummy_data_name,
                image=File(f, name=image_filename)
            )

        print(f'Successfully created CategorySuggest: {suggest.name}, Image Filename: {image_filename}')

def seed_brand(num_rows=None):
    brand_file = os.path.join(csv_dir, 'dummy_brand.csv')
    brand_data = read_csv_file(brand_file)

    if num_rows is not None:
        brand_data = brand_data[:num_rows]

    categories = seed_category()
    seed_suggest()
    for row in brand_data:
        image_filename = row['image_filename']
        dummy_data_name = row['dummy_data_name']
        image_path = os.path.join(settings.STATIC_ROOT, 'images', 'brand', image_filename)

        with open(image_path, 'rb') as f:
            brand = Brand.objects.create(
                name=dummy_data_name,
                image=File(f, name=image_filename)
            )

        print(f'Successfully created Brand: {brand.name}, Image Filename: {image_filename}')
        num_categories = random.randint(1, min(3, len(categories)))
        brand_categories = random.sample(categories, num_categories)
        for category in brand_categories:
            BrandCategory.objects.get_or_create(
                brand=brand,
                category=category
            )

def seed_flag_option():
    flag_types = ['New', 'Feature', 'Sale']
    flag_instances = []
    for name in flag_types:
        flag_option, created = FlagOption.objects.get_or_create(name=name)
        flag_instances.append(flag_option)
    return flag_instances

def seed_product(n):
    flag_instances = seed_flag_option()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    product_file = os.path.join(csv_dir, 'dummy_product.csv')
    product_data = read_csv_file(product_file)
    #product_data = random.sample(product_data, n) if n is not None else product_data
    #product_data_cycle = itertools.cycle(product_data)
    num_rows = len(product_data)

    #for row in product_data:
    if num_rows == 0:
        print("Error: The 'dummy_product.csv' file is empty.")
        return

    for _ in range(n):
        if num_rows == 0:
            # Reset the rows iterator if all rows have been used
            product_data = read_csv_file(product_file)
            num_rows = len(product_data)

        row = random.choice(product_data)
        product_data.remove(row)
        num_rows -= 1
        
        fake_subtitle = "Elevate Your Culinary Creations with the Finest Selection of Locally-Sourced, Artisanal Ingredients, Carefully Curated to Inspire Delicious Meals and Delight Your Palate"
        fake_description = "Experience the epitome of freshness with our hand-picked selection of succulent fruits and vegetables. Sourced from local farms, our produce is grown with care and harvested at the peak of ripeness to ensure optimum flavor and nutrition. From the vibrant hues of crisp apples to the tender leafy greens, each item is carefully inspected to meet our stringent quality standards. Whether you're preparing a refreshing salad or a wholesome stir-fry, our premium ingredients will elevate your culinary creations to new heights. Embrace the essence of farm-to-table goodness and savor the taste of nature's bounty with every delicious bite."
        
        name = row['name']
        subtitle = fake_subtitle
        sku = fake.random_int(min=1000, max=9999)
        description = fake_description
        price = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
        image_filename = row['image_filename']
        flag = random.choice(flag_instances)
        quantity = random.randint(1, 100)
        category_name = random.choice(categories).name
        brand_name = random.choice(brands).name

        image_path = os.path.join(settings.STATIC_ROOT, 'images', 'product', image_filename)
        with open(image_path, 'rb') as f:
            product = Product.objects.create(
                name=name,
                subtitle=subtitle,
                sku=sku,
                description=description,
                price=price,
                image=File(f, name=image_filename),
                flag=flag,
                quantity=quantity,
                slug=slugify(name)
            )

            category = Category.objects.filter(name=category_name).first()
            brand = Brand.objects.filter(name=brand_name).first()
            if category is not None:
                product.category = category
            if brand is not None:
                product.brand = brand
            product.save()

            # add the specified tags to the product
            tag_names = ["Organic", "Fruits", "Chilis"]
            num_tags = random.randint(1, 3)
            selected_tags = random.sample(tag_names, num_tags)
            for tag_name in selected_tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                product.tags.add(tag)

            product_image_dict = {}
    
            # Read product images from CSV
            product_img_file = os.path.join(csv_dir, 'product_img.csv')
            product_images = read_csv_file(product_img_file)
            
            num_images = min(5, len(product_images))
            # create a list of image paths for this product
            product_image_paths = random.sample(product_images, num_images)
            product_image_dict[product] = product_image_paths
            #product_image_list.append((product, product_image_paths)) if [] not {}

            # add some additional images to the product
            for row in product_image_paths:
                image_filename = row['image_filename']
                image_path = os.path.join(settings.STATIC_ROOT, 'images', 'product_img', image_filename)
                with open(image_path, 'rb') as f:
                    product_image = ProductImage.objects.create(
                        product=product,
                        image=File(f, name=image_filename)
                    )

    print(f'Successfully seeded {n} products.')

# seed_category()
# seed_brand()
# seed_product(30)
