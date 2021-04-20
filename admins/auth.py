from django.http import HttpResponse
from django.shortcuts import redirect


def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/login')

    return wrapper_function
