from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def login_user(request):
    if request.method == 'POST':
        # Getting from post request
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # Checking if the user exists in database
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            # Checking if user is active or not
            if user is None:
                return redirect('login_user')
            else:
                # Calling login function and redirect to home page
                login(request, user)
                return redirect('list_of_todo')

        else:
            messages.error(request, 'Username or password does not matched!')
    else:
        print("This is not POST method")
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')
