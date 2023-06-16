from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_list,name="list_of_todo"),
    path('delet_todo_list/<int:id>', views.delete_todo,name="delete_todo"),
    path('create_todo_list',views.create_todo,name="create_todos")
]

# www.todo.com/do_list/list-of-todo/
