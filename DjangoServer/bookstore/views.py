from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.response import Response
#from django.views import Response

def hello(request):
    template = loader.get_template('intro.html')
    return HttpResponse(template.render())


def book_detail(request, id):
    book = Book.objects.get(id = id)
    template = loader.get_template('book_detail.html')
    context = {
    'book': book,
    }
    return HttpResponse(template.render(context, request))

def all_books(request):
    template = loader.get_template('all_books.html')
    print(Book.objects.all().values())
    context = {
        'book' : Book.objects.all().values()
    }
    return HttpResponse(template.render(context, request))

class Books(generics.ListCreateAPIView):
    
    serializer_class = BookSerializer

    def get(self, request, format = None):
        name = request.query_params.get('name')
        if(name != None):
            queryset = Book.objects.filter(name__exact = name)
        else:
            queryset = Book.objects.all()
        return Response(self.serializer_class(queryset, many = True).data, status=status.HTTP_200_OK)    

class BooksUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_fields = "pk"



class Genres(generics.ListCreateAPIView):
    serializer_class = GenreSerializer

    def get(self, request, format = None):
        genre = request.query_params.get('genre')
        if(genre != None):
            queryset = Genre.objects.filter(genre__exact = genre)
        else:
            queryset = Genre.objects.all()
        return Response(self.serializer_class(queryset, many = True).data, status=status.HTTP_200_OK)  

class GenresUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_fields = "pk"


class BookGenres(generics.ListCreateAPIView):
    serializer_class = BookGenreSerializer
    def get(self, request, format = None):
        genre = request.query_params.get('genre')
        book = request.query_params.get('book')
        if(book == None and genre == None):
            queryset = BookGenre.objects.all()
        elif(book != None and genre != None):
            queryset = BookGenre.objects.filter(book__exact = book, genre__exact = genre)
        elif(genre != None):
            queryset = BookGenre.objects.filter(genre__exact = genre)
        else:
            queryset = BookGenre.objects.filter(book__exact = book)

        return Response(self.serializer_class(queryset, many = True).data, status=status.HTTP_200_OK) 
    
    def delete(self, request, format = None):
        genre = request.data.get('genre')
        book = request.data.get('book')
        if(book != None):
            if(genre != None):
                BookGenre.objects.filter(book__exact = book, genre__exact = genre).delete()
            else:
                BookGenre.objects.filter(book__exact = book).delete()

        return Response(status=status.HTTP_204_NO_CONTENT) 

class BookGenresUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    lookup_fields = "pk"


class Users(generics.ListCreateAPIView):
    serializer_class = UserSerializer


class UsersUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_fields = "pk"