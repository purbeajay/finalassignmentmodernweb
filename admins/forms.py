from django import forms
from products.models import Product, User, Cart, Customer, OrderPlaced
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = OrderPlaced
        fields = '__all__'

        widgets = {
            'status' : forms.Select(attrs={'class': 'form-control'})
        }
