from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    #avaible Books
    num_instances_avaible = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genre = Genre.objects.all().count()
    casmurro = Book.objects.filter(title__exact='C').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avaible': num_instances_avaible,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'casmurro': casmurro
    }
    return render(request, 'index.html', context=context)




def listar_livros(request):
    livros = Book.objects.all()
    return render(request, 'lista-livros.html', {'livros': livros})




#class BookListView(generic.ListView):
   # model = Book
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # #template_name = 'book_list.html'  # Specify your own template name/location
 
    # def get_context_data(self, **kwargs):

    #     context =  super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just  some data'
    #     return context


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


<<<<<<< HEAD
# class BookDetailView(generic.DetailView):
#     model = Book


# def book_detail_view(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
    
#     except book.DoesNotExist:
#         raise Http404('Livro nao existe')

#     return render(request, 'catalog/book_detail.html', context={'book': book})


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', context={'book': book})
    

class AuthorListView(generic.ListView):
    model = Author
    def get_contex_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context




def author_detail_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'catalog/author_detail.html', context={'author': author})
=======

""" 
def BookDetailView(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'catalog/book_detail.html', context={'book': book}) """


def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/book_detail.html', context={'book': book})
>>>>>>> 851f360360b4640b8e6f95d8c5d6dd277c8741d3
