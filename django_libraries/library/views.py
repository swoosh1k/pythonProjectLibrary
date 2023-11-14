from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *



class HomeView(ListView):
    model = Library
    context_object_name = 'Libraries'
    template_name = 'library/index.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context






class LibraryDetail(DetailView):
    model = Library
    slug_field = 'slug'
    template_name = 'library/library_detail.html'


    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Library.name
        return context



class AuthorDetail(DetailView):
    model = Author
    slug_field = 'slug'
    template_name = 'library/author_detail.html'

    def get_context_data(self,*, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Author.name
        return context


class BookListView(ListView):
    model = Book
    template_name = 'library/book_d.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.get(pk = self.kwargs['pk_id'])


    def get_context_data(self,* ,object_list = None, **kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = Book.title
        return context




