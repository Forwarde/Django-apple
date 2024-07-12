from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


def index(request):
    tasks=Task.objects.order_by('-id')
    return render(request,'main/index.html',{'title':'Главная страница сайта','tasks':tasks})

def about(request):
    return render(request,'main/about.html')

def login(request):
    return render(request,'main/registration/login.html')

def register(request):
    return render(request,"main/register.html")


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'main/create.html',context)


