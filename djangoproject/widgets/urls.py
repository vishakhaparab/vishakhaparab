from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('calculator', views.calculator, name = 'calculator'),
    path('todolist', views.todolist, name = 'todolist'),
    path('tasktable', views.tasktable, name = 'tasktable'),
    path('delete/<str:tasktitle>', views.delete, name='delete'),
]
