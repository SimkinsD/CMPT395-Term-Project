from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import MyUser, Family, Teacher
from . models import Person


#class UserForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('first_name', 'last_name', 'email')


#class FamilyForm(forms.ModelForm):
#    class Meta:
#        model = Family
#        fields = ('family_name')


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