from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import ListTodo, Category
from django.views.generic import TemplateView

def Login_view(request):
    print(UserLoginForm(request.POST))
    if (request.method == 'POST' and ('username' in request.POST and 'password' in request.POST)):
        print('hello-1')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('hello-2')
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            print('hello-3')
            messages.info(request, f'account done not exit plz sign in')
    else:
        print('hello-4')
        form = AuthenticationForm()
        #return render(request, 'user / login.html', {'form': form, 'title': 'log in'})
        return render(request, 'registration/Login.html')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('registration/Login.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

def todo_view(request):

    todos = ListTodo.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = ListTodo(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            return redirect("/ToDo.html")
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
            for todo_id in checkedlist:
                todo = ListTodo.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo
    return render(request, "ToDo.html", {"todos": todos, "categories": categories})



