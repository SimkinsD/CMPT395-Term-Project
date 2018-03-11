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
    FamilyID = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.account_name



class Child(models.Model):
    ChildID = models.AutoField(primary_key=True)
    Family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    classroom = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Volunteer(models.Model):
    VolunteerID = models.AutoField(primary_key=True)
    Family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



class Signup(models.Model):
    SignupID = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    classroom = models.CharField(max_length=15)
    Volunteer = models.ForeignKey(Volunteer, on_delete= models.CASCADE)

    def __str__(self):
        return self.sID

