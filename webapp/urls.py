from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_review, name='add_review'),
    path('edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
]
