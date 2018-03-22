from django.db import models

class SignUp(models.Model):
    classroom = models.name = models.CharField(max_length=15)
    startTime = models.TimeField(blank = True, null = True)
    endTime = models.TimeField(blank = True, null = True)
    emailReminder = models.BooleanField(default = True)
    
    day = models.CharField(max_length=35)
    

    def __str__(self):
        return "Classroom: " + self.classroom + "Start time: " + self.startTime.__str__() + "\nEnd Time:" + self.endTime.__str__()
