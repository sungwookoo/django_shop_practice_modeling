from django.contrib import admin

# Register your models here.
from product.models import Product, Category, ProductOrder, UserOrder, OrderStatus

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductOrder)
admin.site.register(UserOrder)
admin.site.register(OrderStatus)
