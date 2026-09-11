from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Author, BookInstance, Genre

# Create your views here.


@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count
    num_genres = Genre.objects.count

    # case insensitive regex filter
    num_books_with_teacher = Book.objects.filter(
        title__iregex=r'teacher').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_teacher': num_books_with_teacher
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


# Book_List 'Function' version
# def book_list(request):
#     """Books list (index) using function based view"""
#     book_list = Book.objects.all()
#     context = {'book_list': book_list}
#     return render(request, 'book_list.html', context=context)

# Book_List 'Class' version
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'books'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'books/my_arbitrary_template_name_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["num_books"] = Book.objects.count()
        return context

# Book_Detail 'Function' version
# def book_detail(request, pk):
#     """Book detail view using function based view"""
#     book = Book.objects.get(pk=pk)
#     context = {'book': book}
#     return render(request, 'catalog/book_detail.html', context=context)

# Book_details 'Class' version
class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book

# Book_Create 'Function' version
# def book_create(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("book-detail", pk=book.pk)
#     else:
#         form = BookForm()

#     context = {"form": form}

#     return render(request, "catalog/book_form.html", context=context)

# Create, Update, and Delete class views
class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    success_url = reverse_lazy('books')

# Author_List 'Function' version
class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    context_object_name = "authors"
    paginate_by = 5

# Author_details 'Class' version
class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )
