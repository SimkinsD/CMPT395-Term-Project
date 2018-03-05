from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import MyUser, Teacher
from . models import Person

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['username', 'email']

class MyTeacherCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = ['username', 'email']

class EditUserForm(forms.ModelForm):
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    class Meta(UserChangeForm.Meta):
        model = MyUser
        fields = ['last_name', 'email']   