from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import MyUserCreationForm, MyTeacherCreationForm, EditUserForm
from django.db import models
from . models import Person
from . models import MyUser

class Registor(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('registor')
    template_name = 'registor.html'

class RegistorTeacher(generic.CreateView):
    form_class = MyTeacherCreationForm
    success_url = reverse_lazy('registor_teacher')
    template_name = 'registor_teacher.html'

class AddPerson(CreateView):
    model = Person
    success_url = reverse_lazy('person')
    template_name = 'add_person.html'
    fields = ['user','name', 'hours']

class ViewFamily(generic.ListView):
    model = Person
    template_name = 'family.html'

class PasswordChange(generic.CreateView):
    template_name = 'password_change.html'

class EditUser(generic.UpdateView):
    model = MyUser
    form_class = EditUserForm
    template_name = "edit_user.html"
    success_url = reverse_lazy('home')    
    def get_object(self, queryset=None):
        return self.request.user