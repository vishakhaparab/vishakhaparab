from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from matplotlib.style import context
from TodoApp.forms import Todoform
from TodoApp.models import Todo
from django.contrib import messages
from matplotlib import widgets
from django.contrib.auth.decorators import login_required


@login_required(login_url='todologin')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = Todoform()
        todos = Todo.objects.filter(user = user)
        return render (request,'todoindex.html', context = {'form': form, 'todos': todos})


def todologin(request):
    if request.method == "GET":
        form = AuthenticationForm(request)
        form.fields['username'].widget.attrs['class'] = "form-control"
        form.fields['password'].widget.attrs['class'] = "form-control"
        context = {"form" : form}
        return render (request,'todologin.html', context = context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('todoindex')
        else:
            form = AuthenticationForm(request)
            form.fields['username'].widget.attrs['class'] = "form-control"
            form.fields['password'].widget.attrs['class'] = "form-control"
            context = {"form" : form}
            messages.info(request, 'Enter correct username and password')
            return render (request,'todologin.html', context = context)
            #return render (request,'todologin.html', context = context)


def todologout(request):
    logout(request)
    return redirect("todologin")




def todosignup(request):
    if request.method == "GET":
        form = UserCreationForm(request.POST)
        form.fields['username'].widget.attrs['class'] = "form-control"
        form.fields['password1'].widget.attrs['class'] = "form-control"
        form.fields['password2'].widget.attrs['class'] = "form-control"
        context = {"form" : form}
        return render (request,'todosignup.html', context= context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {"form" : form}
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('todoindex')
        else:
            messages.info(request, 'Enter password with more than 8 digits and include symbols and alphabets')
            return redirect('todosignup')


@login_required(login_url='todologin')
def addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = Todoform(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo.status)
            return redirect("todoindex")
        else:
            return render (request,'todoindex.html', context = {'form': form})


def deletetodo(request, id):
    Todo.objects.get(pk = id).delete()
    return redirect('todoindex')


def changestatustodo(request, id, status):
    todo = Todo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('todoindex')