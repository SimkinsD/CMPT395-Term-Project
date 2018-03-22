from django import forms
from user.models import Signup as SignUp

class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ("classroom","start_time", "end_time",)
    
