from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', INDEX, name='read'),
    path('add/', ADD, name='add'),
    path('edit/', EDIT, name='edit'),
    path('update/<str:id>', UPDATE, name='update'),
    path('delete/<str:id>', DELETE, name='delete'),
]
