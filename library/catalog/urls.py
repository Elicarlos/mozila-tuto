from django.urls import path, re_path
from . import views

urlpatterns = [

    
    path('', views.index, name='index'),
    #path('books/', views.listar_livros, name='books'),

    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    #re_path(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name= 'book-detail')
    re_path(r'^books/(?P<pk>\d+)/$', views.book_detail_view, name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^authors/(?P<pk>\d+)/$', views.author_detail_view, name='author-detail'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.book_detail_view, name= 'book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    
]


