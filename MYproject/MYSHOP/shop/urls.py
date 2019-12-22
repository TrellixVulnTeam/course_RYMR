from django.urls import path
from . import views
from django.conf.urls import url

app_name = "shop"
urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.post_list, name="search"),
    path('books/', views.books, name="books"),
    path('authors/', views.authors, name="authors"),
    path('genres/', views.genres, name="genres"),
    # url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^book/(?P<pk>\d+)$', views.exp_book, name='book-detail'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^signup/$', views.signup, name='signup'),
    path('profile/', views.profile, name="profile"),
    path('basket_adding/', views.basket_adding, name="basket_adding"),
]
