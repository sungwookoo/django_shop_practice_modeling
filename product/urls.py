from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'product'
urlpatterns = [
    path('list', views.categorize_product, name='list'),  # http://127.0.0.1:8000/product/list (GET)
    path('list/<str:category_name>', views.categorize_product, name='list'),

    path('<int:id>/<str:product_name>', views.product_detail, name='product_detail'),

    # product_order
    path('order', views.product_order, name='product_order')

]
