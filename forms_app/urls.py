from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addEntry, name='add'),
    path('edit/<int:pk>/', views.editEntry, name='edit'),
    path('delete/<int:pk>/', views.deleteEntry, name='delete')
]