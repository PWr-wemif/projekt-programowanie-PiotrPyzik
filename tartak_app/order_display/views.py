from django.shortcuts import render
from .models import Element, Order, Client
# Create your views her
from django.views.generic import ListView

class OrderListView(ListView):
    queryset = Order.published.all()
    context_object_name = 'orders'
    paginate_by = 3
    template_name = 'order_display/order_list.html'
    
def order_detail_view(request, order):
    order = Order.objects.get(slug=order)
    