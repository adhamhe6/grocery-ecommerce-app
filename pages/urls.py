from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'pages'
urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home_index.html'), name='index'),
    path('home-index/', TemplateView.as_view(template_name='pages/home_index.html'), name='home_index'),
    path('home-category/', TemplateView.as_view(template_name='pages/home_category.html'), name='home_category'),
    path('home-classic/', TemplateView.as_view(template_name='pages/home_classic.html'), name='home_classic'),
    path('home-grid/', TemplateView.as_view(template_name='pages/home_grid.html'), name='home_grid'),
    path('home-standard/', TemplateView.as_view(template_name='pages/home_standard.html'), name='home_standard'),
]