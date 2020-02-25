from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.models import User

class ProfilePage(TemplateView):
    template_name = 'profile.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

# class ListMembers(ListView):
#     model = User
#     template_name = 'listMembers.html'

class HomePage(TemplateView):
    template_name = "index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse("profile"))
    #     return super().get(request, *args, **kwargs)


def user_list(request):
  users = User.objects.all()
  return render(request, 'listMembers.html', {'users': users})