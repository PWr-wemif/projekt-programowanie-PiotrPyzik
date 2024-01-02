from django.shortcuts import render, redirect, HttpResponse
from .models import Element, Order, Client
from .forms import ElementForm, OrderForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

class OrderListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    queryset = Order.published.all()
    context_object_name = 'orders'
    paginate_by = 3
    template_name = 'order_display/order_list.html'

@login_required(login_url='/login/')   
def order_detail_view(request, order):
    order = Order.objects.get(slug=order)
    elements = order.element.all().order_by('status')
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
    
@login_required(login_url='/login/')
def client_detail_view(request, client):
    client = Client.objects.get(slug = client)
    return render(request, 'order_display/order_detail.html')

@login_required(login_url='/login/')
def element_edit_view(request, element):
    element = Element.objects.get(slug = element)
    if request.method=='POST':
        element_form = ElementForm(request.POST, instance=element)
        if element_form.is_valid():
            element.save()
            return redirect(element.order.get_absolute_url())
    else:
        element_form = ElementForm(instance=element)
        
    return render(request, 'order_display/element_edit.html', {'element_form': element_form})


def new_order(request):
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            messages.success(request, "utworzono nowe zamówienie")
            order = form.save()
            return redirect(order.get_absolute_url())
        else:
            messages.ERROR(request, "coś poszło nie tak")
            return render(request, 'order_display/new_order.html', {'form': form})
    form = OrderForm()
    return render(request, 'order_display/new_order.html', {'form': form})

def test(request):
    return render(request, 'order_display/searchbar.html')


def show_searches(request):
    
    data = request.GET['search']
    print(data)
    searches = Client.objects.filter(
        Q(first_name__contains=data) | 
        Q(last_name__contains=data)
    )
    print(searches)
    return JsonResponse({'searches':list(searches.values())})


def finnish_element(request, element):
    element = Element.objects.get(slug = element)
    if element.status == Element.Status.DONE:
        element.status = Element.Status.IN_PROGRESS
    else: 
        element.status = Element.Status.DONE
    element.save()
    return redirect(element.order.get_absolute_url())