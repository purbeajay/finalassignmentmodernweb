import only as only
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from admins.auth import admin_only

import products
from admins.forms import ProductForm, UserForm, CartForm, CustomerForm, OrderForm
from products.models import Product, Customer, Cart, OrderPlaced

@admin_only
def admin_dashboard(request):
    return render(request, "admins/admin_dashboard.html")


def show_user(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, "admins/show_users.html", context)


def add_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return render(request, "admins/show_users.html")
    else:
        context = {
            'UserForm': UserForm,
        }
    return render(request, "admins/add_user.html", context)


def delete_user(request, id):
    print(id)
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()
        return render(request, "admins/show_users.html")


def show_cart(request):
    carts = Cart.objects.all()
    context = {
        'carts': carts,

    }
    return render(request, "admins/show_carts.html", context)


def add_cart(request):
    if request.method == "POST":
        cart = CartForm(request.POST)
        if cart.is_valid():
            cart.save()
        return render(request, "admins/show_carts.html")
    else:
        context = {
            'CartForm': CartForm,
        }
    return render(request, "admins/add_cart.html", context)


def delete_cart(request, id):
    if request.method == 'POST':
        cart = Cart.objects.get(pk=id)
        cart.delete()
        return render(request, "admins/show_carts.html")


def show_customer(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, "admins/show_customer.html", context)


def adminChangeStatus(request, order_id):
    if request.method == "POST":
        order_id = order_id
        order_status = request.POST['status']
        order = OrderPlaced.objects.get(pk=order_id)
        order.status = order_status
        order.save()
        return redirect('show_order')

def show_order(request):
    orderplaced = OrderPlaced.objects.all()
    context = {
        'orderplaced': orderplaced,
        'order_status_form': OrderForm,
    }
    return render(request, "admins/show_order.html", context)


def add_order(request):
    if request.method == "POST":
        order = OrderForm(request.POST)
        if order.is_valid():
            order.save()
        return render(request, "admins/show_order.html")
    else:
        context = {
            'OrderForm': OrderForm,
        }
    return render(request, "admins/add_order.html", context)


def show_product(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "admins/show_product.html", context)


def add_product(request):
    if request.method == "POST":
        title = request.POST['title']
        selling_price = request.POST['selling_price']
        discounted_price = request.POST['discounted_price']
        description = request.POST['description']
        brand = request.POST['brand']
        category = request.POST['category']
        product_image = request.FILES['product_image']
        Product.objects.create(title=title, selling_price=selling_price, discounted_price=discounted_price,
                               description=description, brand=brand, category=category,
                               product_image=product_image).save()
        return render(request, "admins/show_product.html")
    else:
        context = {
            'ProductForm': ProductForm,
        }
        return render(request, "admins/add_product.html", context)


def delete_product(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        product.delete()
        return render(request, "admins/show_product.html")


def add_customer(request):
    if request.method == "POST":
        customer = CustomerForm(request.POST)
        print(customer)
        if customer.is_valid():
            print("valid")
            customer.save()
        return render(request, "admins/show_customer.html")
    else:
        context = {
            'CustomerForm': CustomerForm,
        }
    return render(request, "admins/add_customer.html", context)


def delete_customer(request, id):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return render(request, "admins/show_customer.html")
