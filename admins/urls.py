from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name="admin_dashboard"),
    path('show_user/', views.show_user, name="show_user"),
    path('show_cart/', views.show_cart, name="show_cart"),
    path('show_customer/', views.show_customer, name="show_customer"),
    path('show_order/', views.show_order, name="show_order"),
    path('show_product/', views.show_product, name="show_product"),
    path('add_product/', views.add_product, name="add_product"),
    path('add_user/', views.add_user, name= "add_user"),
    path('add_cart/', views.add_cart, name = "add_cart"),
    path('add_customer/', views.add_customer, name = "add_customer"),
    path('add_order/', views.add_order, name = "add_order"),
    path('delete_product/<int:id>/', views.delete_product, name="delete_product"),
    path('admin_change_status/<int:order_id>/', views.adminChangeStatus, name="adminChangeStatus"),
    path('delete_customer/<int:id>/', views.delete_customer, name="delete_customer"),
    path('delete_user/<int:id>/', views.delete_user, name="delete_user"),
    path('delete_cart/<int:id>/', views.delete_cart, name="delete_cart"),

]
