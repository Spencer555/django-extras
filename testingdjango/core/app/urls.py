from django.urls import path 
from app.views import book_list, BookCreateView, book_detail



urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:pk>', book_detail, name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
]