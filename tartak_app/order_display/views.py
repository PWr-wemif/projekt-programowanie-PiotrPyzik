from django.shortcuts import render, redirect
from .models import Element, Order, Client
from .forms import ElementForm, OrderForm
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
        print("POST")
        if 'element_form' in request.POST:
            element_form = ElementForm(request.POST)
            order_form = OrderForm()
            if element_form.is_valid():
                element = element_form.save(commit=False)
                element.order = order
                element.save()
        if 'order_form' in request.POST:
            order_form = OrderForm(request.POST, instance = order)
            element_form = ElementForm()
            if order_form.is_valid():
                order = order_form.save()
        return redirect(order.get_absolute_url())
    else:
        element_form = ElementForm()
        order_form=OrderForm(instance = order)
        

    return render(request, 'order_display/order_detail.html', {"order":order,"elements":elements, "element_form": element_form,'order_form':order_form})
    
    
def client_detail_view(request, client):
    client = Client.objects.get(slug = client)
    return render(request, 'order_display/order_detail.html')

def element_edit_view(request, element):
    element = Element.objects.get(slug = element)
    
    if request.method=='POST':
        element_form = ElementForm(request.POST)
        if element_form.is_valid():
            element.save()
    else:
        element_form = ElementForm()
    return render(request, 'order_display/element_edit.html', {'element_form': element_form})
    
    