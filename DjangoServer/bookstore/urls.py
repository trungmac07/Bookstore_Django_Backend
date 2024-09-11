from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='bookstore'),
    path('all_books', views.all_books, name='all_books'),
    path('book_detail/<int:id>', views.book_detail, name='book_detail'),
    path('api/books/', views.Books.as_view(), name='books'),
    path('api/books/<int:pk>/', views.BooksUpdate.as_view(), name='books_update'),
    path('api/genres/', views.Genres.as_view(), name='genres'),
    path('api/genres/<int:pk>/', views.GenresUpdate.as_view(), name='genres_update'),
    path('api/bookgenres/', views.BookGenres.as_view(), name='bookgenres'),
    path('api/bookgenres/<int:pk>/', views.BookGenresUpdate.as_view(), name='bookgenres_update'),

    path('api/login/', views.LoginAPIView.as_view(), name='login'),
    path('api/signup/', views.SignUpAPIView.as_view(), name='signup'),

]