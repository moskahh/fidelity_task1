"""fidelity_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from django.conf.urls import url
from django.urls import path

from . import views
from ecar import EmployeeOperation, CarOperation, RecordOperation

urlpatterns = [
    # path第一个分配网站地址，后调用函数
    url(r'^$', views.mainpage),
    # Employee
    path('showEmployee/', EmployeeOperation.show),
    path('editEmployee/<int:sid>/', EmployeeOperation.edit),
    path('deleteEmployee/<int:sid>/', EmployeeOperation.delete),
    path('addEmployee/', EmployeeOperation.add),
    path('findcar/<int:id>/', EmployeeOperation.findcar),
    # path('mainpage/', views.mainpage),

    #car
    path('addCar/', CarOperation.add),
    path('showCar/', CarOperation.show),
    path('deleteCar/<int:cid>/', CarOperation.delete),
    path('editCar/<int:cid>/', CarOperation.edit),

    #record
    path('showRecord/', RecordOperation.show),
    path('carEnter/', RecordOperation.carenter),
    path('carLeave/', RecordOperation.carleave),
    path('deleteRecord/<int:sid>/', RecordOperation.delete),



]
