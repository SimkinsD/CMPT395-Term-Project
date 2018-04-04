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
    model = FieldTripSignup
    template_name = 'current_field_trips.html'
    current = datetime.date.today()
    all_trips = FieldTripSignup.objects.filter(trip__date__gte=current)

    def __init__(self):
        self.trips = self.all_trips


# Needs work
class SignupFieldTrip(CreateView):
    model = FieldTripSignup
    success_url = reverse_lazy('signup_field_trip')
    template_name = 'signup_field_trip.html'
    fields = ('trip', 'volunteer', 'classroom')



    



