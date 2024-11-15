from typing import Set
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views import generic


# Create your views here.


class CustomLogInView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('base:tasks')
    
class logout(generic.View):
    def get(request):
        logout(request)
        return redirect('base:login')
        

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:tasks')
    template_name = 'base/task_create.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:tasks')
    template_name = 'base/task_create.html'

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('base:tasks')



    












