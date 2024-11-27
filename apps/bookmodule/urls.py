from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search/', views.search, name="books.search" ),
    path('simple/query', views.simple_query, name="books.simple_query" ),
    path('complex/query', views.complex_query, name="books.complex_query" ),
    path('lab8/task1', views.books_under_50, name='books.task1'),
    path('lab8/task2', views.books_task2, name='books.task2'),
    path('lab8/task3', views.books_task3, name='books.task3'),
    path('lab8/task4', views.books_task4, name='books.task4'),
    path('lab8/task5', views.books_task5, name='books.task5'),
    path('lab8/task7', views.students_per_city, name='students_per_city'),
]   