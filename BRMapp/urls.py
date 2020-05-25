from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('view-books', views.viewBook),
    url('edit-book', views.editBook),
    url('delete-book', views.deleteBook),
    url('search-book', views.searchBook),
    url('new-book', views.newBook),
    url('add', views.add),
    url('search', views.search),
    url('edit', views.edit),
    url('login', views.userLogin),
    url('logout', views.userLogout),

]