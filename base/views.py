from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url=reverse_lazy('tasks')








