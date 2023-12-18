from django.urls import path
from . import views

app_name = 'worker_app'
urlpatterns = [
   path('', views.order_list, name='order_list'),
]