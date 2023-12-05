from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(LoginRequiredMixin, CreateView):
    login_url = "login"
    success_url = reverse_lazy('users:profile') #on form success, take user back to profile.
    model = CustomUser
    template_name = "users/userProfile.html"
    form_class = CustomUserCreationForm
