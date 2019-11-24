from django.http import HttpResponse
from django.shortcuts import render
from .models import OnlineShopperTable, ToDoList
from django.db.models import Count
from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

def Home(request):
    Rev_True = OnlineShopperTable.objects.all().filter(Revenue='TRUE').count()
    Rev_False = OnlineShopperTable.objects.all().filter(Revenue='FALSE').count()
    context = {
        'True_Val': Rev_True,
        'False_Val': Rev_False
    }
    return render(request, 'home.html', context)


def index(request):
    todos = ToDoList.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            # category = request.POST["category_select"]
            content = title + " -- " + date  # + " " + category
            Todo = ToDoList(title=title, content=content, due_date=date)
            Todo.save()
            return redirect("/")
        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = ToDoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "ToDo.html", {"todos": todos})


def register(request):
    form = UserCreationForm
    return render(request=request,
                  template_name="registration/login.html",
                  context={"form": form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})