# Online Bookstore - Django Backend

This is a **Django-backend-based online bookstore** application that allows users to browse, search, and purchase books online. The backend is built using **Django** and **Django REST framework**, providing a comprehensive RESTful API for handling various bookstore-related functionalities.

## Features

- Browse a catalog of books
- Search books by title, author, genre, or ISBN
- User authentication (registration, login, and logout)
- Add books to shopping cart
- Checkout and order processing
- Admin panel to manage books, orders, and users

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/trungmac07/Bookstore_Django_Backend
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

The application is now running at `http://localhost:8000/`.

## API Endpoints

| Method | Endpoint                 | Description                   |
|--------|--------------------------|-------------------------------|
| GET    | /api/books/               | List all books                |
| GET    | /api/books/{id}/          | Retrieve a single book        |
| POST   | /api/cart/                | Add book to cart              |
| GET    | /api/cart/                | View cart items               |
| POST   | /api/order/               | Checkout and create an order  |
| POST   | /api/register/            | Register a new user           |
| POST   | /api/login/               | Login an existing user        |
| GET    | /api/bookgenres/          | List all book genres          |
...    
