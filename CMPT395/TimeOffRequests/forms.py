from django import forms
from .models import TimeOffRequest
from user.models import Volunteer, Family


class DateInput(forms.DateInput):
    input_type = 'date'

class RequestTimeOffForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(RequestTimeOffForm, self).__init__(*args, **kwargs)
    #     self.initial['family'] = Volunteer.getCurrent(self).family

    class Meta:
        model = TimeOffRequest
        fields = ( 'start_date', 'end_date','reason_for_time_off',)
        widgets = {'start_date':DateInput(), 'end_date':DateInput()}