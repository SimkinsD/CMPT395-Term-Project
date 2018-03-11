from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . forms import MyUserCreationForm, MyTeacherCreationForm
from . models import MyUser, Person, Teacher, ChooseFacilitator

class PersonInline(admin.TabularInline):
    model = Person

class MyUserAdmin(UserAdmin):
    model = MyUser
    add_form = MyUserCreationForm
    inlines = [
        PersonInline,
    ]

class TeacherAdmin(UserAdmin):
    model = Teacher
    add_form = MyTeacherCreationForm

class PersonAdmin(admin.ModelAdmin):
  list_display = ('user', 'name', 'hours')

class ChooseFacilitatorAdmin(admin.ModelAdmin):
  list_display = ('name', 'hours')
    
admin.site.register(Person, PersonAdmin)
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ChooseFacilitator, ChooseFacilitatorAdmin)