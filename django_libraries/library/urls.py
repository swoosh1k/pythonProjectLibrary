from django.urls import path
from .views import *



urlpatterns = [
    path('', HomeView.as_view(), name = 'main'),
    path('library/<slug:slug>/', LibraryDetail.as_view(), name = 'library_detail'),
    path('author/<slug:slug>/', AuthorDetail.as_view(), name = 'author_detail'),
    path('book/<int:pk_id>/', BookListView.as_view(), name = 'book_detail')


]