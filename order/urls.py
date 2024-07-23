from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:id>/', views.order, name="orders"),
    path('invoice/<int:id>', views.invoice, name="invoice"),
    path('tracking', views.tracking, name="tracking"),
    path('details/<int:id>', views.order, name="order_details"),
    path('delete/<int:id>', views.delete, name="delete_order"),
]