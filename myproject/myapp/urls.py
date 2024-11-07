from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/new/', views.item_create, name='item_create'),
    path('item/<int:id>/edit/', views.item_update, name='item_update'),
    path('item/<int:id>/delete/', views.item_delete, name='item_delete'),
]
