from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.utils import timezone
import pytz
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import User
from .components.signup_form import SignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse

from .permission import *
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

class BooksAPIView(generics.ListCreateAPIView):
    
    authentication_classes = [JWTAuthentication]
    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'PUT']:
            return [IsAuthenticated(), IsAdmin()]  # Only admins
        else:
            return [IsAuthenticated()]  # Clients can view books
    
    
    serializer_class = BookSerializer

    def get(self, request, format = None):
        name = request.query_params.get('name')
        if(name != None):
            queryset = Book.objects.filter(name__exact = name)
        else:
            queryset = Book.objects.all()
        return Response(self.serializer_class(queryset, many = True).data, status=status.HTTP_200_OK)    

class BooksUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_fields = "pk"

class GenresAPIView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer

    def get(self, request, format = None):
        genre = request.query_params.get('genre')
        if(genre != None):
            queryset = Genre.objects.filter(genre__exact = genre)
        else:
            queryset = Genre.objects.all()
        return Response(self.serializer_class(queryset, many = True).data, status=status.HTTP_200_OK)  

class GenresUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_fields = "pk"


class BookGenresAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    def get(self, request, format = None):
        genre = set(int(genre_id) for genre_id in request.query_params.get('genre').split(','))
       
        if(genre):
            book_ids = BookGenre.objects.filter(genre_id__in=genre).values('book_id')
            queryset = Book.objects.filter(id__in=book_ids).distinct().order_by('id')
            #queryset = BookGenre.objects.filter(book__exact = book, genre__exact = genre)
            return Response(self.serializer_class(queryset, many = True).data, status=status.HTTP_200_OK) 
        else:
            queryset = Book.objects.all()
            #queryset = BookGenre.objects.filter(book__exact = book, genre__exact = genre)
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

class BookGenresUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    lookup_fields = "pk"


class UsersAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer


class UsersUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_fields = "pk"
    
    
class SignUpAPIView(APIView):

    def post(self, request):
        
        form = SignUpForm(request.data)
        
        
        if form.is_valid():
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']

            # Create and save the user
            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                date_of_birth=date_of_birth,
                address=address,
                phone_number=phone_number
            )
            user.set_password(password)  # Hash the password
            user.save()

            #messages.success(request, 'Sign up successful')
            data = {"message":"Sign up successfully"}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {"message":"Error occurred", "error" : form.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                #print(user)
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'message' : f"Log in successfully - Welcome {user.email}",
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'role' : str(user.role)
                }
                return Response({**data, "user_id" : user.id}, status=status.HTTP_200_OK)
            data = {'message' :"Log in unsuccessfully - email or password is incorrect"}    
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        data = {'message' : "Log in unsuccessfully - email or password is incorrect", 'error' : serializer.errors}    
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    
####### CART #################################

class CartAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def post(self, request):
  
        try:
            order_data = request.data.get("order_details", [])
            user_id = request.data.get("user_id")
            
            total = 0
            for order in order_data:
                book = Book.objects.get(pk = order["book"])
                total += book.price * order["amount"]
            
            new_order = Order(user_id = user_id, total = total)
            new_order.save()

            for order in order_data:
                book = Book.objects.get(pk = order["book"])
                detail = OrderDetail(order = new_order, book = book, amount = order["amount"], price = book.price, total = book.price * order["amount"])
                detail.save()
            
            return Response("Order successfully !", status=status.HTTP_201_CREATED)
        except:
            return Response("An error occurred while creating the order", status=status.HTTP_400_BAD_REQUEST)