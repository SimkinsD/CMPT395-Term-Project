from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import MyUserCreationForm, EditUserForm

from django.http import HttpResponseRedirect

from django.db import models
from . models import MyUser, Family, Volunteer, Child


class RegistorView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('registor')
    template_name = 'registor.html'

class AddVolunteerView(CreateView):
    model = Volunteer
    success_url = reverse_lazy('volunteer')
    template_name = 'add_volunteer.html'
    fields = ['VolunteerID', 'Family', 'first_name', 'last_name']

class AddFamilyView(CreateView):
    model = Family
    success_url = reverse_lazy('family')
    template_name = 'add_family.html'
    fields = ['user', 'FamilyID', 'account_name', 'email', 'phone']

class AddChildView(CreateView):
    model = Child
    success_url = reverse_lazy('child')
    template_name = 'add_child.html'
    fields = ['ChildID', 'Family', 'first_name', 'last_name']


class ChooseVolunteerView(generic.ListView):
    model = Volunteer
    template_name = 'select_volunteer.html'

    def get_queryset(self):
        familyID = Family.objects.filter(user=self.request.user).values_list('FamilyID', flat=True)[0]
        volunteer = Volunteer.objects.filter(Family__FamilyID=familyID)
        return volunteer

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs) 
        names = dict()
        for name in data['volunteer_list']:
            n = list()
            n.append(name.first_name)
            n.append(name.VolunteerID)
            names[name.first_name] = n
        data['name_list'] = names
        return data

    def post(self, request):
        if 'volunteer' in request.POST:
            volunteer_id = request.POST['volunteer']
            volunteer = Volunteer.objects.get(pk=volunteer_id)
            family_id = volunteer.Family.FamilyID
            #family = Family.objects.get(pk=family_id)
            Family.objects.filter(pk=family_id).update(current_volunteer=volunteer_id)
        return HttpResponseRedirect(self.request.path_info)

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