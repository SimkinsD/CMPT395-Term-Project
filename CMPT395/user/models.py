from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db import models
from django.conf import settings


class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
    objects = MyUserManager()

#class Teacher(MyUser):
#    objects = MyUserManager()
#    class Meta:
#        verbose_name = 'Teacher'
#        verbose_name_plural = 'Teachers'

#class Person(models.Model):
#    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#    name = models.CharField(max_length=32)
#    hours = models.FloatField(default=5.0)
    
#    def __str__(self):
#        return self.name

#class Children(models.Model):
#    name = models.CharField(max_length=30)
#    class_room = models.CharField(max_length=30)

''' 
This class extends Django's existing User info using MyUser
'''
class Family(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    familyID = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True)
    current_volunteer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.family_name



class Child(models.Model):
    childID = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    classroom = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Volunteer(models.Model):
    volunteerID = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True)


    def getCurrent(view):
        family = Family.objects.get(user=view.request.user)
        return Volunteer.objects.get(volunteerID=family.current_volunteer)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



class Signup(models.Model):
    signupID = models.AutoField(primary_key=True)
    date = models.DateField(["%Y-%m-%d"], blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=15)
    volunteer = models.ForeignKey(Volunteer, blank=True, null=True, on_delete= models.CASCADE)

    def __str__(self):
        return (str(self.date) + " " + str(self.start_time) + " ID: " + str(self.signupID))

    
