from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *


class NewAccount(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username', 'is_staff', 'email')




#class MyUserCreationForm(UserCreationForm):
#    email = forms.EmailField(required=True)
#    class Meta(UserCreationForm.Meta):
#        model = MyUser
#        fields = ['username', 'email']

#class MyTeacherCreationForm(UserCreationForm):
#    email = forms.EmailField(required=True)
#    class Meta(UserCreationForm.Meta):
#        model = Teacher
#        fields = ['username', 'email']