from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import UserAuthForm


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect("order_display:order_list")
        else:
            return HttpResponse("nie kurwa")
    else:
        form = UserAuthForm()
        return render(request, 'users/login.html', {'login_form':form})
    
    
    