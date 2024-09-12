from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    
    genres = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'price', 'love', 'buy', 'left', 'discount', 'image', 'genres']
        
    def get_genres(self, obj):
        book_genres = BookGenre.objects.filter(book_id__exact=obj).values_list('genre')
        print(book_genres)
        genres = Genre.objects.filter(id__in=book_genres).order_by('genre')
        #print( [genre.genre for genre in genres])
        return [genre.genre for genre in genres]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ShortGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = '__all__'
        unique_together = (('book', 'genre'))


class LoveBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoveBook
        fields = '__all__'
        unique_together = (('user', 'book'))


class CommentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBook
        fields = '__all__'
        unique_together = (('user', 'book'))


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        unique_together = (('user', 'book'))


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
        unique_together = (('order', 'book'))
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)