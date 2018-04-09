# DJANGO IMPORTS
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.db.models import Q
from django.db import models

# PYTHON IMPORTS
import datetime

# APP IMPORTS
from . models import MyUser, Family, Volunteer, Child, TimeTransfer
from .forms import MyUserCreationForm, EditUserForm, TimeTransferForm

class SearchUserView(generic.ListView):
    template_name = "search_user.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        family_list = Family.objects.all()
        if(query):
            family_list = family_list.filter(
                Q(family_name__icontains=query) |
                Q(phone__icontains=query) |
                Q(email__icontains=query)
                )
        return family_list

class RegistorView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('registor')
    template_name = 'registor.html'

class AddVolunteerView(CreateView):
    model = Volunteer
    success_url = reverse_lazy('volunteer')
    template_name = 'add_volunteer.html'
    fields = ['volunteerID', 'family', 'first_name', 'last_name']

class AddFamilyView(CreateView):
    model = Family
    success_url = reverse_lazy('family')
    template_name = 'add_family.html'
    fields = ['user', 'familyID', 'family_name', 'email', 'phone']

class AddChildView(CreateView):
    model = Child
    success_url = reverse_lazy('child')
    template_name = 'add_child.html'
    fields = ['childID', 'family', 'first_name', 'last_name']


class ChooseVolunteerView(generic.ListView):
    model = Volunteer
    template_name = 'select_volunteer.html'

    def get_queryset(self):
        familyID = Family.objects.filter(user=self.request.user).values_list('familyID', flat=True)[0]
        volunteer = Volunteer.objects.filter(family__familyID=familyID)
        return volunteer

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs) 
        names = dict()
        for name in data['volunteer_list']:
            n = list()
            n.append(name.first_name)
            n.append(name.volunteerID)
            names[name.first_name] = n
        data['name_list'] = names
        return data

    def post(self, request):
        if 'volunteer' in request.POST:
            volunteer_id = request.POST['volunteer']
            volunteer = Volunteer.objects.get(pk=volunteer_id)
            family_id = volunteer.family.familyID
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

class TimeTransferView(generic.TemplateView):
    template_name = "time_transfer.html"
    model = TimeTransfer
    transfer_form = TimeTransferForm
    transfers = TimeTransfer.objects.all()

    def update(self):
        self.transfers = TimeTransfer.objects.all()

    def post(self, request, *args, **kwargs):
        if "add-transfer" in request.POST:
            tt_form = self.transfer_form(request.POST)
            if tt_form.is_valid():
              th = tt_form.save(commit=False)
              th.date = datetime.date.today()
              th.from_family = Family.objects.get(user=request.user)
              th.save()
        
        self.update()
        return render(request, self.template_name, {"view" : self})