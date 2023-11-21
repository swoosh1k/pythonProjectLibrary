from django.urls import path
from .views import *



urlpatterns = [
    path('', HomeView.as_view(), name = 'main'),
    path('filter_all', Filter_All.as_view(), name = 'filter_all'),
    path('review/<int:pk>', AddReview.as_view(), name = 'add_review'),
    path('pricefilter/<int:pk>/', PriceFilter.as_view(), name = 'price_filter'),
    path('book/<int:pk_id>/', BookListView.as_view(), name='book_detail'),
    path('findbook/', BookFind.as_view(), name = 'book_find'),
    path('delete/<int:pk>/', DeleteReview, name = 'delete'),
    path('library/<slug:slug>/', LibraryDetail.as_view(), name = 'library_detail'),
    path('author/<slug:slug>/', AuthorDetail.as_view(), name = 'author_detail'),
    path('addpost/', AddPost.as_view(), name = 'add_post'),
    path('login/', Login.as_view(), name = 'login'),
    path('register/', Register.as_view(), name = 'register')


]