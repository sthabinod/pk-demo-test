from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user,name="login_user"),
    path('logout/', views.logout_user,name="logout_user"),
]

# www.todo.com/do_list/list-of-todo/
