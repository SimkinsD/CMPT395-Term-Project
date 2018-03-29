from django.db import models
from user.models import Family

class TimeOffRequest(models.Model):
    family = models.ForeignKey(Family, on_delete = models.CASCADE)
    start_date = models.DateField(blank = False)
    end_date = models.DateField(blank = False)
    reason_for_time_off = models.TextField(max_length = 300)
    def __str__(self):
        return "TimeOffRequest|" + "Family:" + str(family) + " Start date:" + str(self.start_date) +\
         "| End Date:" + str(self.end_date) + "\n"
