from django.urls import path
from . import views

app_name = 'order_display'

urlpatterns = [
    path('', views.OrderListView.as_view(), name = "post_list"),
    path('<slug:order>/', views.order_detail_view, name = 'order_detail'),
    
]