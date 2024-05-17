from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.homepage, name='home'),
    path('allproducts/', views.productspage, name='productspage'),
    path('productdetails/<int:product_id>', views.product_detail, name='productdetail'),
]