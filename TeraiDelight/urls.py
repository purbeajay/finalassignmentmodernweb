from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

import products


def index(request):
    return HttpResponse("this is the final assignment")

urlpatterns = [
    path('admin/', include("admins.urls")),
    path('', include('products.urls'))
]