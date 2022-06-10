from enum import Enum

from django.db import models

# Create your models here.
from user.models import User


class Category(models.Model):
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=256)


# <상품 이름, 상품 카테고리, 이미지, 설명, 가격, 재고량>
class Product(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='media/product/')
    desc = models.TextField()
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 유저가 주문한 상품의 개수를 저장
class ProductOrder(models.Model):
    class Meta:
        db_table = "product_order"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)


# 유저의 주문(배송주소, 주문시간, 전체 상품 가격, 할인율, 최종가격, 유효여부(boolean))을 저장
class UserOrder(models.Model):
    class Meta:
        db_table = "user_order"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receiving_address = models.CharField(max_length=256)
    total_price = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    amount = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)
    final_price = models.IntegerField(default=0)

    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 주문한 상태(주문 완료, 결제 완료, 취소, 배송출발, 배송완료) 을 저장
class OrderStatus(models.Model):
    class Meta:
        db_table = "order_status"

    status = models.CharField(max_length=256)
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
