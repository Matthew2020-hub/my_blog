from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
# Create your views here.
