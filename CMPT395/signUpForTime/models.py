from django.db import models

class signUp(models.Model):
    classroom = models.name = models.CharField(max_length=15)
    startTime = models.TimeField(blank = True, null = True)
    endTime = models.TimeField(blank = True, null = True)
    emailReminder = models.BooleanField(default = True)

    def __str__(self):
        return "Classroom:" + self.classroom + " \nStart time:" + self.startTime + " \nEnd Time:" + self.endTime

