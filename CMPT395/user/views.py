from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import MyUserCreationForm, MyTeacherCreationForm
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


def ViewFamily(request):
    user_obj = MyUser.objects.get(id=request.user.id)
    person_obj = user_obj.person_set.all()
    print(user_obj)
    print(person_obj)
    context = {'user_obj':user_obj, 'person_obj':person_obj}
    return render(request, 'family.html', context)