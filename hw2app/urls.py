from django.urls import path
from .views import history_of_orders, products_form


urlpatterns = [
    path('history_of_orders/', history_of_orders, name='history_of_orders'),
    path('products_form/', products_form, name='products_form'),
]