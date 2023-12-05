from django.urls import path
from . import views

app_name = 'order_display'
urlpatterns = [
    path('', views.OrderListView.as_view(), name = "post_list"),
    path('szczegoly/<slug:order>/', views.order_detail_view, name = 'order_detail'),
    path('klient/<slug:client>/', views.client_detail_view, name = 'client_detail'),
    path('edit/<slug:element>', views.element_edit_view, name = 'element_edit'),
]