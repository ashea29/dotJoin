from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.

class UserRegister(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"


# def sign_up(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('project_list')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})