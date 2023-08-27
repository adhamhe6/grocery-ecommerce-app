from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models import Q
from django.db.models.aggregates import Avg
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    sku = models.IntegerField(_('SKU'))
    subtitle = models.CharField(_('Subtitle'), max_length=500)
    description = models.TextField(_('Description'), max_length=10000)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    image = models.ImageField(_('Image'), upload_to='products/products/')
    quantity = models.IntegerField(_('Quantity'))
    flag = models.ForeignKey('FlagOption', related_name='products', verbose_name=_('Flag'), 
                    on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey('Brand', related_name='products', verbose_name=_('Brand'), 
                    on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', related_name='products', verbose_name=_('Category'), 
                    on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager()
    #slug = models.SlugField(allow_unicode=True, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @receiver(pre_save, sender='products.Product')
    def generate_slug(sender, instance, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.name)

    @property
    def avg_review(self):
        avg = self.reviews.aggregate(avg=Avg('rate'))
        return avg['avg']

class FlagOption(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    
    class Meta:
        verbose_name = _('Flag')
        verbose_name_plural = _('Flags')

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', verbose_name=_('Product'), on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='products/product_images/')

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
    
    def __str__(self):
        return str(self.product)

class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to='products/brands/')
    category = models.ManyToManyField('Category', related_name='brands', verbose_name=_('Category'), through='BrandCategory')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to='products/categories/')
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
    
class CategorySuggest(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to='products/category_images/')
    
    def __str__(self):
        return self.name

class BrandCategory(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    
    class Meta:
        verbose_name = _('Brand & Category')
        verbose_name_plural = _('Brands & Categories')
        
    def __str__(self):
        return f'{self.brand.name} - {self.category.name}'

class ProductReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews',verbose_name=_('User'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews',verbose_name=_('Product'), on_delete=models.CASCADE)
    rate = models.IntegerField(_('Rate'), validators=[MaxValueValidator(5), MinValueValidator(0)])
    review = models.TextField(_('Review'), max_length=500)
    created_at = models.DateTimeField(_('Created at'), default=timezone.now)
    
    class Meta:
        verbose_name = _('Product Review')
        verbose_name_plural = _('Product Reviews')

    def __str__(self):
        return str(self.user)