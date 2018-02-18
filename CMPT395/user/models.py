from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings

class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
    objects = MyUserManager()

class Teacher(MyUser):
    objects = MyUserManager()
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class Person(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,)
    name = models.CharField(max_length=32)
    hours = models.FloatField(default=5.0)
    
    def __str__(self):
        return self.name

    