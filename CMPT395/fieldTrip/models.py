from django.db import models
from user.models import Volunteer


class FieldTrip(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    info = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.title


class FieldTripSignup(models.Model):
    trip = models.OneToOneField(FieldTrip, on_delete=models.CASCADE)
    volunteer = models.ManyToManyField(Volunteer)
    classroom = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.trip, self.volunteer)



