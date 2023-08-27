from django.views.generic import ListView, DetailView
from .models import Product, Brand, Category
from django.db.models.aggregates import Count

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 12
    
    def get_template_names(self):
        template_names = ['products/shop_1_col.html', 'products/shop_2_col.html', 'products/shop_3_col.html', 'products/shop_4_col.html', 'products/shop_5_col.html']
        return template_names

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class BrandListView(ListView):
    model = Brand
    template_name = 'products/brand_list.html'
    context_object_name = 'brands'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all().annotate(product_count=Count('products'))
        return context

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'products/brand_detail.html'
    context_object_name = 'brand'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        #context["products"] = brand.products.filter(brand=brand)
        context["products"] = Product.objects.filter(brand=brand)
        return context
    
class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'