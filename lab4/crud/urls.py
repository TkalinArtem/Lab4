from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('create', views.create, name = 'create'),
    path('read/', views.read, name='read_books'),
    path('update/<int:book_id>/', views.update, name='update_book'),
    path('delete/<int:book_id>/', views.delete, name='delete_book'),
]