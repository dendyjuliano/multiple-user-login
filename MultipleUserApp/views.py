from django.shortcuts import render
from django.contrib.auth import login
from .models import *
from django.views.generic import CreateView, ListView, UpdateView
from .forms import *

# Create your views here.
class Register(CreateView):
    model = User
    form_class = UserRegister
    template_name = 'register.html'

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
