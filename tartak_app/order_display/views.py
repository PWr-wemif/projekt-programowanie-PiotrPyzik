from django.shortcuts import render
from .models import Element, Order, Client
# Create your views her
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Order.published.all()
    context_object_name = 'orders'
    paginate_by = 3
    template_name = 'order_display/main.html'