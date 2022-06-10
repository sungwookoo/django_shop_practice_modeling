from django.shortcuts import render, redirect

# Create your views here.
from product.models import Category, Product


def home(request):
    category = Category.objects.first()
    category_name = category.name
    redirect('/product/list/' + category_name)


def get_list(request, category_name):
    if request.method == 'GET':
        category = Category.objects.get(name=category_name)
        product_list = Product.objects.filter(category=category)
        return render(request, 'index.html', {product_list: product_list})
