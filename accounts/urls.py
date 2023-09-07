from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.sign_in, name='sign_in'),
    path('logout/', views.sign_out, name='sign_out'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('password_reset/done/', views.password_reset_done_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('password_reset/complete/', views.password_reset_complete_view, name='password_reset_complete'),
    path('password_change/', views.password_change_view, name='password_change'),
    path('password_change/done/', views.password_change_done_view, name='password_change_done'),
]