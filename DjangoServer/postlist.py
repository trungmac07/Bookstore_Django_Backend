import requests
from db import books

book = books()

for i in book[1:]:
    x = requests.post('http://localhost:8000/books/', data = i)
    print(x.text)
    #break



