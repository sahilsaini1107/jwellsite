from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('orders/', OrderList.as_view()),
    path('address/', AddressList.as_view()),
    path('cart/', CartList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]