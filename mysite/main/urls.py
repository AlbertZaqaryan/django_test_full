from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('review/', views.review, name='review'),
    path('product/', views.product, name='product'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('detele_product/', views.detele_product, name='detele_product'),
]