from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

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



class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    queryset = Book.objects.filter(title__icontains='war'[:5])
    template_name = 'books/my_arbitrary_templates_name_list.html'