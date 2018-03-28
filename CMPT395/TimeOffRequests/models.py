from django.db import models
from user.models import Family

class TimeOffRequest(models.Model):
    # family = models.ForeignKey(Family, on_delete = models.CASCADE)
    start_date = models.DateField(blank = False)
    end_date = models.DateField(blank = False)
    reason_for_time_off = models.TextField()
