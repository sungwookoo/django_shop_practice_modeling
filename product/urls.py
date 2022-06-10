from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('product/list/<str:category_name>', views.get_list, name='get_list'),
]