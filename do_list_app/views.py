from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def show_list(request):
    
    # select * from todo;
    todos = Todo.objects.all()
    
    return render(request,"todo/show_todo_list.html",{"todos_key":todos})
@login_required
def delete_todo(request,id):
    # delete from todo where id=id
    Todo.objects.get(id=id).delete()
    return redirect("list_of_todo")

@login_required
def create_todo(request):
    
    if request.method=="POST":    
    # title
        title = request.POST.get('title')
    # descirption
        description = request.POST.get('description')
        
    # save
        Todo.objects.create(title=title,description=description)
    
    # redirect
        return redirect("list_of_todo")
    return render(request,'todo/create_todo.html')