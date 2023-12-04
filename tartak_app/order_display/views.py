from django.shortcuts import render, redirect
from .models import Element, Order, Client
from .forms import ElementForm
from django.views.generic import ListView

class OrderListView(ListView):
    queryset = Order.published.all()
    context_object_name = 'orders'
    paginate_by = 3
    template_name = 'order_display/order_list.html'
    
def order_detail_view(request, order):
    order = Order.objects.get(slug=order)
    elements = order.element.all()
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.order = order
            element.save()
            return redirect(order.get_absolute_url())
    else:
        form = ElementForm()

    return render(request, 'order_display/order_detail.html', {"order":order,"elements":elements, "form": form})
    
    
def client_detail_view(request, client):
    client = Client.objects.get(slug = client)
    pass