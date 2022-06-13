from django.db import models
from django.urls import reverse

from user import models as user_models


class Category(models.Model):
    # category_1.name
    name = models.CharField(max_length=100) # laptop, mobile

    class Meta:
        db_table = "categories"

    # category_1.get_absolute_url
    def get_absolute_url(self):
        print("get_url = ", end=""), print(reverse('product:list', args=[self.name]))
        return reverse('product:list', args=[self.name]) # product/list/laptop


# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # laptop, mobile
#     name = models.CharField(max_length=100)  # macbook, thinkpad
#     image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True )
#     description = models.TextField(blank=True)
#
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = "products"
#
#     def __str__(self):
#         return self.name

class OrderStatus(models.Model):
    status_name = models.CharField(max_length=100)  # 주문 완료, 결제 완료, 취소, 배송출발, 배송완료

    class Meta:
        db_table = "order_status"


class ProductOrder(models.Model):
    # product row one
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    product_count = models.IntegerField()
    user_order = models.ForeignKey('UserOrder', on_delete=models.SET_NULL, blank=True,null=True)

    class Meta:
        db_table = 'product_orders'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # laptop, mobile
    name = models.CharField(max_length=100)  # macbook, thinkpad
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True )
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('product:product_detail', args=[self.id, self.name])


class UserOrder(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.SET_NULL, null=True)
    product_order = models.ForeignKey('ProductOrder', on_delete=models.SET_NULL, null=True)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)

    delivery_address = models.CharField(max_length=1000)
    order_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2)
    final_price = models.DecimalField(max_digits=20, decimal_places=2)

    active = models.BooleanField()

    class Meta:
        db_table = 'user_order'
