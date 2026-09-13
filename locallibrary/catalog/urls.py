from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path("book/create/", views.BookCreateView.as_view(), name="book-create"),
    path("book/<int:pk>/update/", views.BookUpdateView.as_view(), name="book-update"),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name="book-delete"),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path("author/create/", views.AuthorCreateView.as_view(), name="author-create"),
    path("author/<int:pk>/update/", views.AuthorUpdateView.as_view(), name="author-update"),
    path("author/<int:pk>/delete/", views.AuthorDeleteView.as_view(), name="author-delete"),
    path("genres/", views.GenreListView.as_view(), name="genres"),
    path("genre/<int:pk>/", views.GenreDetailView.as_view(), name="genre-detail"),
    path("genre/create/", views.GenreCreateView.as_view(), name="genre-create"),
    path("genre/<int:pk>/update/", views.GenreUpdateView.as_view(), name="genre-update"),
    path("genre/<int:pk>/delete/", views.GenreDeleteView.as_view(), name="genre-delete"),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    
]