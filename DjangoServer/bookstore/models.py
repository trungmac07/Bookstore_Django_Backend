from django.db import models


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


class User(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=6)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.username

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



