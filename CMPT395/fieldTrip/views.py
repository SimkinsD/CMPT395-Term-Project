from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from . models import *
from . forms import *
from user.models import *
import datetime



class CreateFieldTrip(CreateView):
    form_class = CreateFieldTripForm
    success_url = reverse_lazy('create_field_trip')
    template_name = "field_trip.html"



class CurrentTrip(ListView):
    model = FieldTrip
    template_name = 'current_field_trips.html'
    context_object_name = 'trip_list'


# Needs work
class SignupFieldTrip(CreateView):
    form_class = SignupFieldTripForm
    success_url = reverse_lazy('signup_field_trip')
    template_name = 'signup_field_trip.html'



    



