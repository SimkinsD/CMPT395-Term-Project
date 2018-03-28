from django import forms
from .models import TimeOffRequest


class DateInput(forms.DateInput):
    input_type = 'date'

class RequestTimeOffForm(forms.ModelForm):

    class Meta:
        model = TimeOffRequest
        # Use commented out "fields" variable when adding family.
        # fields = ('family', 'start_date', 'end_date','reason_for_time_off',)
        fields = ('start_date', 'end_date','reason_for_time_off',)
        widgets = {'start_date':DateInput(), 'end_date':DateInput()}