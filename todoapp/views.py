from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from todoapp.models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    