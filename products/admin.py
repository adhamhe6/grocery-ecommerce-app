from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage, Brand, Category, CategorySuggest, BrandCategory, ProductReview, FlagOption

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5
    
    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0  # Set extra to 0 when updating a Category instance
        return self.extra

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    list_filter = ('brand', 'category', 'flag')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="30" height="30"/>', obj.image.url)
        else:
            return '-'
    image_preview.short_description = 'Image'
    list_display = ['name', 'sku', 'price', 'quantity', 'image_preview', 'flag']
    
class BrandCategoryInline(admin.TabularInline):
    model = BrandCategory

class BrandAdmin(admin.ModelAdmin):
    inlines = [BrandCategoryInline]
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="30" height="30"/>', obj.image.url)
        else:
            return '-'
    image_preview.short_description = 'Image'
    list_display = ['name', 'image_preview']
 
class CategorySuggestAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.image:
            return format_html('<div style="width: 35px; height: 25px; border-radius: 50%; overflow: hidden;"><img src="{}" width="100%" height="100%"/></div>', obj.image.url)
        else:
            return '-'

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
    list_display = ['name', 'image_preview']

class CategoryAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="30" height="30"/>', obj.image.url)
        else:
            return '-'
    image_preview.short_description = 'Image'
    list_display = ['name', 'image_preview']
    
class BrandCategoryAdmin(admin.ModelAdmin):
    list_filter = ('brand', 'category')
    
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rate', 'created_at')
    
class FlagOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategorySuggest, CategorySuggestAdmin)
admin.site.register(BrandCategory, BrandCategoryAdmin)
admin.site.register(FlagOption, FlagOptionAdmin)