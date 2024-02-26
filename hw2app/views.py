from django.shortcuts import render, redirect
from .models import OrderModel
from django.utils import timezone
from django.utils.timezone import timedelta
from .forms import ProductForms

# Create your views here.
def history_of_orders(request):
    client_id = 2
    orders_last_7_days = OrderModel.objects.filter(customer_id=client_id, date_order__gte=timezone.now() - timedelta(days=7))
    orders_last_30_days = OrderModel.objects.filter(customer_id=client_id, date_order__gte=timezone.now() - timedelta(days=30))
    orders_last_365_days = OrderModel.objects.filter(customer_id=client_id,date_order__gte=timezone.now() - timedelta(days=365))

    context = {
        'orders_last_7_days': orders_last_7_days,
        'orders_last_30_days': orders_last_30_days,
        'orders_last_365_days': orders_last_365_days,
    }

    return render(request, 'hw2app/history_of_orders.html', context)

def products_form(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
 #           return redirect('product_list')
    else:
        form = ProductForms()
    return render(request, 'hw2app/products_form.html', {'form': form})
