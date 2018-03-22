from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . forms import MyUserCreationForm
from . models import MyUser, Family, Child, Volunteer, Signup

class FamilyInline(admin.TabularInline):
    model = Family

#class VolunteerInline(admin.TabularInline):
#    model = Volunteer

class ChildInline(admin.TabularInline):
    model = Child

class MyUserAdmin(UserAdmin):
    model = MyUser
    add_form = MyUserCreationForm
    inlines = [
        FamilyInline,
    ]
    
class FamilyAdmin(admin.ModelAdmin):
  list_display = ('user', 'family', 'family_name')
  inlines = [
      #VolunteerInline,
      ChildInline,
  ]

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("volunteerID", "first_name")

class ChildAdmin(admin.ModelAdmin):
    list_display = ("childID", "family", "first_name")

    
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Child, ChildAdmin)