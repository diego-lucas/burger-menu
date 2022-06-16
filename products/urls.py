from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.index, name='index'),
    path('<int:product_id>', views.product, name='product'),
]
