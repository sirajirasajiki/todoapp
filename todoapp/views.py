from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from todoapp.models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(CreateView):
    model = Task
    fields = "__all__" # ['user', 'title']
    success_url = reverse_lazy("tasks")

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__" # ['user', 'title']
    success_url = reverse_lazy("tasks")