from django.shortcuts import render
from django.views import generic
from user.models import *
import datetime


class FamilyStats(generic.ListView):
    template_name = 'family_stats.html'
    model = Signup

    def __init__(self):
        self.total = self.week_hours()

    """ Using the current date it gets the entire weeks hours for selected family.
        It returns a timedelta object of the current hours and minutes volunteered that week.
    """
    def week_hours(self):
        total = datetime.timedelta(hours=0)
        week = datetime.date.today()
        offset = week.weekday()
        # Gets the beginning and end dates based on current date
        begin_week =  week - datetime.timedelta(days=offset)
        end_week = week + datetime.timedelta(days=(6 - offset))
        family = Family.objects.get(user=5)#self.request.user)
        signups = Signup.objects.filter(volunteer__family__familyID = family.familyID)

        # Goes through each signup for the family and calculates total hours for the week
        for day in signups:
            end = datetime.timedelta(hours=day.end_time.hour,minutes=day.end_time.minute)
            start = datetime.timedelta(hours=day.start_time.hour,minutes=day.start_time.minute)
            total = total + (end - start)
        return total









