from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import RequestTimeOffForm
from django.urls import reverse
from user.models import Volunteer

# Create your views here.

class TimeOffRequestView(TemplateView):
    template_name = 'time_off_request.html'

    def get(self, request):
        request_time_off_form = RequestTimeOffForm()
        return render(request, self.template_name, {'request_time_off_form':request_time_off_form})
    
    def post(self, request):
        request_time_off_form = RequestTimeOffForm(request.POST)
        if request_time_off_form.is_valid():
            currentRequest = request_time_off_form.save(commit=False)
            currentRequest = Volunteer.getCurrent(self).family
            currentRequest.save()
            return redirect(reverse('weeklyCalendar'))
        
        return render(request, self.template_name, {'request_time_off_form':request_time_off_form})
