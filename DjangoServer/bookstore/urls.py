from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='bookstore'),
    path('all_books', views.all_books, name='all_books'),
    path('book_detail/<int:id>', views.book_detail, name='book_detail'),
    path('books/', views.Books.as_view(), name='books'),
    path('books/<int:pk>/', views.BooksUpdate.as_view(), name='books_update'),
    path('genres/', views.Genres.as_view(), name='genres'),
    path('genres/<int:pk>/', views.GenresUpdate.as_view(), name='genres_update'),
    path('bookgenres/', views.BookGenres.as_view(), name='bookgenres'),
    path('bookgenres/<int:pk>/', views.BookGenresUpdate.as_view(), name='bookgenres_update'),


]