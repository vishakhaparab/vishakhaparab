from asyncio import tasks
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from matplotlib.pyplot import title
from widgets.models import task

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def calculator(request):
    return render(request, 'calculator.html')

def todolist(request):
    context = {'success': False}
    if request.method == "POST":
        tktitle = request.POST['title']
        tkdesc = request.POST['desc']
        ins = task(tasktitle = tktitle, taskdesc = tkdesc)
        ins.save()
        context = {'success': True}
    return render(request, 'todolist.html', context)

def tasktable(request):
    alltasks = task.objects.all()
    context = {'tasks': alltasks}
    return render(request, 'tasktable.html', context)

def delete(request, tasktitle):
    tk = task.objects.get(tasktitle = tasktitle)
    tk.delete()
    return HttpResponseRedirect(reverse('tasktable'))

