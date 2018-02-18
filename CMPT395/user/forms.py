from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import MyUser
from . models import Person

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['username', 'email']