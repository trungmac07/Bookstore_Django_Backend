import requests
from db import *

#book = books()

# for i in book:
#     x = requests.post('http://localhost:8000/api/books/', data = i, headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTM4NDYwLCJpYXQiOjE3MjYxMjc2NjAsImp0aSI6ImM4MTVmYzI4ZGRmNzQwMWI5MmVjMGRhM2ZlZGUwMjdjIiwidXNlcl9pZCI6Mn0._gmY0-0FTI0XDqUILYChJDoycTy86WHK12lW_LHd2fQ'})
#     print(x.text)
#     #break

# genre = genres()

# for i in genre:
#     x = requests.post('http://localhost:8000/api/genres/', data = i, headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTM4NDYwLCJpYXQiOjE3MjYxMjc2NjAsImp0aSI6ImM4MTVmYzI4ZGRmNzQwMWI5MmVjMGRhM2ZlZGUwMjdjIiwidXNlcl9pZCI6Mn0._gmY0-0FTI0XDqUILYChJDoycTy86WHK12lW_LHd2fQ'})
#     print(x.text)

book_genre = book_genres()

def postbookgenre():
  
    for i in book_genre:
        x = requests.post('http://localhost:8000/api/bookgenres/', data = i, headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTM4NDYwLCJpYXQiOjE3MjYxMjc2NjAsImp0aSI6ImM4MTVmYzI4ZGRmNzQwMWI5MmVjMGRhM2ZlZGUwMjdjIiwidXNlcl9pZCI6Mn0._gmY0-0FTI0XDqUILYChJDoycTy86WHK12lW_LHd2fQ'})
        print(x.text)

postbookgenre()
