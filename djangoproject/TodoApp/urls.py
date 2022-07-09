"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from . import views


urlpatterns = [
    path('', views.home, name= "todoindex"),
    path('todologin/', views.todologin, name="todologin"),
    path('addtodo/', views.addtodo, name="addtodo"),
    path('deletetodo/<int:id>', views.deletetodo, name="deletetodo"),
    path('changestatus/<int:id>/<str:status>', views.changestatustodo, name="changestatustodo"),
    path('todologout/', views.todologout, name="todologout"),
    path('todosignup/', views.todosignup, name="todosignup"),
]
