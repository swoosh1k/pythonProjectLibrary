from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.db.models import Count, Sum, Avg, Max, Min





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
        context['avgprice'] = Book.objects.filter(author__slug = self.kwargs['slug']).aggregate(Avg('price'))
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




class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'library/addpost.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list = None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление книги'
        return context


class Register(CreateView):
    form_class = UserCreationForm
    template_name  = 'library/register.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'library/login.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход в учетную запись'
        return context



def logout_user(request):
    logout(request)
    return redirect('login')



class AddReview(View):
    def post(self,request,pk):
        form = ReviewForm(request.POST)
        book  = Book.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.book= book
            form.save()
        return redirect('/')



def DeleteReview( pk):
    ReviewBook.objects.get(pk = pk).delete()
    return redirect('/')



class PriceFilter(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'использован фильтр для книг'
        return context
    def get_queryset(self):
        return Book.objects.filter(price__in = self.request.GET.getlist('price'), author__id = self.kwargs['pk'])





class BookFind(ListView):
    model = Book
    template_name = 'library/book_d.html'
    context_object_name = 'book'


    def get_context_data(self, *, object_list=None, **kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = Book.title
        return context
    def get_queryset(self):
        return Book.objects.get(title__icontains = self.request.GET.get('q'))