from typing import Any
from django.db import models
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm

from news.models import NewsStory


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(LoginRequiredMixin, generic.DetailView):
    login_url = "login"
    success_url = reverse_lazy('users:profile') #on form success, take user back to profile.
    model = CustomUser
    template_name = "users/userProfile.html"
    form_class = CustomUserCreationForm

    # def get_queryset(self):
    #     return NewsStory.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authored_stories'] = NewsStory.objects.filter(author=self.kwargs['pk']) 
        return context
        