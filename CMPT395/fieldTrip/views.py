from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from . models import *
from user.models import *
import datetime



class CreateFieldTrip(CreateView):
    model = FieldTrip
    success_url = reverse_lazy('create_field_trip')
    template_name = "field_trip.html"
    fields = ('title', 'location', 'info', 'date')
    widgets = {'date' : forms.DateInput}



class CurrentTrip(ListView):
    model = FieldTrip
    template_name = 'current_field_trips.html'
    context_object_name = 'trip_list'
    current = datetime.date.today()
    queryset = FieldTrip.objects.filter(date__gte=current)



# Needs work
class SignupFieldTrip(CreateView):
    model = FieldTripSignup
    success_url = reverse_lazy('signup_field_trip')
    template_name = 'signup_field_trip.html'
    fields = ('trip', 'volunteer', 'classroom')



    



