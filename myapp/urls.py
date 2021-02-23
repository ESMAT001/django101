from . import views
from django.urls import path
urlpatterns = [
    path('', views.index,name="index"),
    path('shortcut/',views.shortcut,name="shortcut"),
    path('items/',views.itemsList,name="itemsList"),
    path('items/<int:item_id>/',views.item,name="item"),
    path('items/add/',views.add_item,name="add_item"),
    path('items/update/<int:id>/',views.update_item,name="update_item"),
    path('items/delete/<int:id>/',views.delete_item,name="delete_item"),
]