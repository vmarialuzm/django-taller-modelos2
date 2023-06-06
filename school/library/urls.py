from django.urls import path
from . import views

urlpatterns = [
    path('',views.BookListView.as_view(),name="index_book"),
    path('booklist/',views.BookList.as_view(),name="booklist"),
    path('bootstrapej/',views.BootstrapEj.as_view(),name="bootstrapej"),
    path('book/<id>',views.select_book,name="select_book"),
]
