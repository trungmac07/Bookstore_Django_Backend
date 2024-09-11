from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils import timezone

class Book(models.Model):
    title = models.TextField(default="")
    author = models.CharField(max_length=255)
    description = models.CharField()
    price = models.IntegerField(default=0)
    love = models.IntegerField(default=0)
    buy = models.IntegerField(default=0)
    left = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    image = models.BinaryField(default=None, null = True)

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('role') != 'admin':
            raise ValueError('Superuser must have role = admin.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default='client')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.BinaryField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.genre

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('book', 'genre'),)
    

class LoveBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField()
    class Meta:
        unique_together = (('user', 'book'),)


class CommentBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField()
    content = models.TextField()
    class Meta:
        unique_together = (('user', 'book'),)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()
    class Meta:
        unique_together = (('user', 'book'),)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    total = models.IntegerField()

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()
    discount = models.FloatField()
    class Meta:
        unique_together = (('order', 'book'),)


