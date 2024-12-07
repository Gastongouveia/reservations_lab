from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('approve/<int:reservation_id>/', views.approve_reservation, name='approve_reservation'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
]