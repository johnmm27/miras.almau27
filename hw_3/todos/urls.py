from django.urls import path
from .views import index_page, todo_details, delete_todo

urlpatterns = [
    # todos/
    path('', index_page, name='index_page'),
    path('<int:pk>/', todo_details, name='todo_details'),
    path('<int:pk>/delete/', delete_todo, name='delete_todo'),
]

