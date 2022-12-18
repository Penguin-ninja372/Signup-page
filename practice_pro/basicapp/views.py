from django.shortcuts import render
from basicapp.forms import UserForm
from django.views.generic import TemplateView, CreateView, ListView
from basicapp.models import User
from django.urls import reverse_lazy

# Create your views here.
class HomePage(TemplateView):
    template_name = "index.html"

class AboutPage(TemplateView):
    template_name = 'about.html'

class UserList(ListView):
    model = User

class NewUserForm(CreateView):
    redirect_field_name = "basicapp/index.html"
    form_class = UserForm

    model = User