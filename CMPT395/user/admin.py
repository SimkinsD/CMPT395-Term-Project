from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . forms import MyUserCreationForm
from . models import MyUser, Person

class PersonInline(admin.TabularInline):
    model = Person

class MyUserAdmin(UserAdmin):
    model = MyUser
    add_form = MyUserCreationForm
    inlines = [
        PersonInline,
    ]

class PersonAdmin(admin.ModelAdmin):
  list_display = ('user', 'name', 'hours')

admin.site.register(Person, PersonAdmin)
admin.site.register(MyUser, MyUserAdmin)