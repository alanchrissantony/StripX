from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account, name="account"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('address/add', views.AddressUser.add, name="add_address"),
    path('address/edit/<int:id>', views.AddressUser.edit, name="edit_address"),
    path('address/delete/<int:id>', views.AddressUser.delete, name="delete_address"),
    path('register/', views.register, name="register"),
    path('verification/', views.verification, name="verification"),
    path('verification/resend', views.send, name="resend"),
    path('password-reset/', views.verify, name="otp"),
    path('password-reset/new-password/', views.password, name="password"),
]