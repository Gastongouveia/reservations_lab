from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_lab, name='add_lab'),
    path('list/', views.list_labs, name='list_labs'),
    path('<int:pk>/edit/', views.edit_lab, name='edit_lab'),
    path('<int:pk>/delete/', views.delete_lab, name='delete_lab'),
]
