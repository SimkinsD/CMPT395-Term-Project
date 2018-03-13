from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import MyUserCreationForm, MyTeacherCreationForm, EditUserForm

from django.http import HttpResponseRedirect

from django.db import models
from . models import MyUser
from . models import Person, ChooseFacilitator


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

class ChooseFacilitatorView(generic.ListView):
    model = Person
    template_name = 'select_facilitator.html'
    success_url = reverse_lazy('home')


    def __init__(self):
        if ChooseFacilitator.objects.all().exists():
            pass
        else:
            ChooseFacilitator.objects.create(name='name', hours=0)

    def post(self, request):
        person_obj = Person.objects.filter(user=self.request.user)
        person_name_list = person_obj.values_list('name', flat=True)
        if 'person' in request.POST:
            name = request.POST['person']
            for n in person_name_list:
                if n == name:
                    hours = person_obj.filter(name=n).values_list('hours', flat=True)[0]
                    if ChooseFacilitator.objects.all().exists():
                        ChooseFacilitator.objects.all().update(name=name)
                        ChooseFacilitator.objects.all().update(hours=hours)
                        
        return HttpResponseRedirect(self.request.path_info)

    def get_queryset(self):
        person_id = Person.objects.filter(user=self.request.user).values_list('name', flat=True)
        return person_id

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs) 
        names = dict()
        for name in data['person_list']:
            names[name] = name

        current_person = ChooseFacilitator.objects.values()[0]
        data['name_list'] = names
        data['current_person'] = current_person
        return data
        
class Home(generic.ListView):
    model = MyUser  
    template_name = 'home.html'


class PasswordChange(generic.CreateView):
    template_name = 'password_change.html'

class EditUser(generic.UpdateView):
    model = MyUser
    form_class = EditUserForm
    template_name = "edit_user.html"
    success_url = reverse_lazy('home')    
    def get_object(self, queryset=None):
        return self.request.user