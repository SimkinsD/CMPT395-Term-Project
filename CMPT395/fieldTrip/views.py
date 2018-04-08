from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from user.models import *
import datetime



class CreateFieldTrip(CreateView):
    form_class = CreateFieldTripForm
    success_url = reverse_lazy('create_field_trip')
    template_name = "field_trip.html"



class CurrentTrip(ListView):
    model = FieldTrip
    template_name = 'current_field_trips.html'

    def get(self, request):
        field_trips = FieldTrip.objects.all()
        field_trip_signups = FieldTripSignup.objects.all()

        return render(request, self.template_name, {'field_trips':field_trips, 'field_trip_signups':field_trip_signups})


# Needs work
class SignupFieldTrip(CreateView):
    form_class = SignupFieldTripForm
    success_url = reverse_lazy('signup_field_trip')
    template_name = 'signup_field_trip.html'



    



