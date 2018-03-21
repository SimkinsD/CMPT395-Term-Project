from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from . forms import *
from django.db import models
from . models import *


#class Registor(generic.CreateView):
#    form_class = NewAccount
#    success_url = reverse_lazy('registor')
#    template_name = 'registor.html'

#class RegistorTeacher(generic.CreateView):
#    form_class = MyTeacherCreationForm
#    success_url = reverse_lazy('registor_teacher')
#    template_name = 'registor_teacher.html'

#class AddPerson(CreateView):
#    model = Person
#    success_url = reverse_lazy('person')
#    template_name = 'add_person.html'
#    fields = ['user','name', 'hours']

#class ViewFamilyOld(generic.ListView):
#    model = Person
#    template_name = 'family.html'

class PasswordChange(generic.CreateView):
    template_name = 'password_change.html'

class UpdateUser(generic.CreateView):
    model = MyUser
    template_name = 'edit_user.html'
    fields = ['first_name', 'last_name', 'email']

#----------------------------------------------

class AddAccount(CreateView):
    form_class = NewAccount
    success_url = reverse_lazy('account')
    template_name = 'add_account.html'

class AddFamily(CreateView):
    model = Family
    success_url = reverse_lazy('family')
    template_name = 'add_family.html'
    fields = ('user', 'family_name', 'phone', 'email')


class AddVolunteer(CreateView):
    model = Volunteer
    success_url = reverse_lazy('volunteer')
    template_name = 'add_volunteer.html'
    fields = ('family', 'first_name', 'last_name', 'phone', 'email')


class AddChild(CreateView):
    model = Child
    success_url = reverse_lazy('child')
    template_name = 'add_child.html'
    fields = ('Family', 'first_name', 'last_name', 'classroom')


class ViewFamily(generic.ListView):
    model = Family
    template_name = 'family.html'

class ViewVolunteer(generic.ListView):
    model = Volunteer
    template_name = 'volunteer.html'

class ViewChild(generic.ListView):
    model = Child
    template_name = 'child.html'

class AddSignup(CreateView):
    model = Signup
    success_url = reverse_lazy('child')
    template_name = 'add_child.html'
    fields = ('date', 'start_time', 'end_time', 'classroom', 'volunteer')