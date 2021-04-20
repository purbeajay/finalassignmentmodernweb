from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [

                  path('', views.ProductView.as_view(), name="home"),
                  path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
                  path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
                  path('cart/', views.show_cart, name='showcart'),
                  path('pluscart/', views.plus_cart, name = "pluscart"),
                  path('minuscart/', views.minus_cart),
                  path('removecart/', views.remove_cart),
                  path('checkout/', views.checkout, name='checkout'),
                  path('address/', views.address, name='address'),
                  path('orders/', views.orders, name='orders'),
                  path('paymentdone/', views.payment_done, name='paymentdone'),

                  path('mobile/', views.mobile, name='mobile'),
                  path('mobile/<slug:data>', views.mobile, name='mobiledata'),

                  path('accounts/login/',
                       auth_views.LoginView.as_view(template_name='product/login.html', authentication_form=LoginForm),
                       name='login'),
                  # path('profile/', views.profile, name='profile'),
                  path('profile/', views.ProfileView.as_view(), name='profile'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
                  path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='product/passwordchange.html',
                                                                                form_class=MyPasswordChangeForm,
                                                                                success_url='/passwordchangedone/'),
                       name='passwordchange'),
                  path('passwordchangedone/',
                       auth_views.PasswordChangeDoneView.as_view(template_name='product/passwordchangedone.html'),
                       name='passwordchangedone'),

                  path("password-reset/", auth_views.PasswordResetView.as_view(template_name='product/password_reset.html',
                                                                               form_class=MyPasswordResetForm),
                       name="password_reset"),
                  path("password-reset/done/",
                       auth_views.PasswordResetDoneView.as_view(template_name='product/password_reset_done.html'),
                       name="password_reset_done"),
                  path("password-reset-confirm/<uidb64>/<token>/",
                       auth_views.PasswordResetConfirmView.as_view(template_name='product/password_reset_confirm.html',
                                                                   form_class=MySetPasswordForm),
                       name="password_reset_confirm"),
                  path("password-reset-complete/",
                       auth_views.PasswordResetCompleteView.as_view(template_name='product/password_reset_complete.html'),
                       name="password_reset_complete"),

                  path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
