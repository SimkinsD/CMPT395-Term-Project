from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from . forms import *
from django.db import models
from . models import *

#class Register(generic.CreateView):
#    form_class = UserForm 
#    success_url = reverse_lazy('registor')
#    template_name = 'registor.html'


class Registor(generic.CreateView):
    form_class = NewAccount
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

class UpdateUser(generic.CreateView):
    model = MyUser
    template_name = 'edit_user.html'
    fields = ['first_name', 'last_name', 'email']


class AddFamily(CreateView):
    model = Family
    success_url = reverse_lazy('person')
    template_name = 'add_person.html'
    fields = ('user', 'account_name', 'phone')


class AddVolunteer(CreateView):
    model = Volunteer
    success_url = reverse_lazy('person')
    template_name = 'add_person.html'
    fields = ('Account', 'first_name', 'phone')