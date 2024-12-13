from django.urls import path
from . import views

urlpatterns = [
     path('add/', views.add_teacher, name='add_teacher'),
    path('list/', views.list_teachers, name='list_teachers'),
    path('<int:pk>/edit/', views.edit_teacher, name='edit_teacher'),
    path('<int:pk>/delete/', views.delete_teacher, name='delete_teacher'),
    path('reservations/', views.my_reservations, name='my_reservations'),
]
