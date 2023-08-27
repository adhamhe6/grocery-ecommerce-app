from django.urls import path
from django.views.generic import TemplateView

app_name = 'products'
urlpatterns = [
    path('shop-5column/', TemplateView.as_view(template_name='products/shop_5_col.html'), name='shop_5_col'),
    path('shop-4column/', TemplateView.as_view(template_name='products/shop_4_col.html'), name='shop_4_col'),
    path('shop-3column/', TemplateView.as_view(template_name='products/shop_3_col.html'), name='shop_3_col'),
    path('shop-2column/', TemplateView.as_view(template_name='products/shop_2_col.html'), name='shop_2_col'),
    path('shop-1column/', TemplateView.as_view(template_name='products/shop_1_col.html'), name='shop_1_col'),
    path('product-tab/', TemplateView.as_view(template_name='products/product_tab.html'), name='product_tab'),
    path('product-simple/', TemplateView.as_view(template_name='products/product_simple.html'), name='product_simple'),
    path('product-video/', TemplateView.as_view(template_name='products/product_video.html'), name='product_video'),
    path('category-list/', TemplateView.as_view(template_name='products/category_list.html'), name='category_list'),
    path('brand-list/', TemplateView.as_view(template_name='products/brand_list.html'), name='brand_list'),
    path('brand-detail/', TemplateView.as_view(template_name='products/brand_detail.html'), name='brand_detail'),
]
