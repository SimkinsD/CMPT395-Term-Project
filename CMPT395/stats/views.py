from django.shortcuts import render
from django.views import generic
from user.models import *
import datetime


class FamilyStats(generic.ListView):
    template_name = 'family_stats.html'
    model = Signup


    def __init__(self):
        self.week_total = self.week_hours(datetime.date.today(), Family.objects.get(user=5))#self.request.user))
        self.month_total = self.month_hours(datetime.date.today(), Family.objects.get(user=5))#self.request.user))
        self.required_hours = self.required_hours(Family.objects.get(user=4))#self.request.user))



    """ Using the current date it gets the entire weeks hours for selected family.
        Return:
            It returns a timedelta object of the current hours and minutes volunteered that week.
        Param: 
            requested_week: is the week you would like the volunteer hours for.
                It must be a datetme.date object of a single day in the requested week.
            requested_family: is the family that you want the weekly hours for.
                It must be a single Family object (from user.models) 
    """
    def week_hours(self, requested_week, requested_family):
        total = datetime.timedelta(hours=0)
        week = requested_week
        offset = week.weekday()
        # Gets the beginning and end dates based on current date
        begin_week =  week - datetime.timedelta(days=offset)
        end_week = week + datetime.timedelta(days=(6 - offset))
        family = requested_family
        signups = Signup.objects.filter(volunteer__family__familyID = family.familyID, 
                                        date__range=(begin_week, end_week))

        # Goes through each signup for the family and calculates total hours for the week
        for day in signups:
            end = datetime.timedelta(hours=day.end_time.hour,minutes=day.end_time.minute)
            start = datetime.timedelta(hours=day.start_time.hour,minutes=day.start_time.minute)
            total = total + (end - start)
        return total



    """ Using the current date it gets the entire month hours for selected family.
        Return:
            It returns a timedelta object of the current hours and minutes volunteered that month.
        Param: 
            requested_month: is the month you would like the volunteer hours for.
                It must be a datetme.date object of a single day in the requested month.
            requested_family: is the family that you want the monthly hours for.
                It must be a single Family object (from user.models)
    """
    def month_hours(self, requested_month, requested_family):
        total = datetime.timedelta(hours=0)
        current = requested_month
        family = requested_family
        signups = Signup.objects.filter(volunteer__family__familyID = family.familyID, 
                                        date__year=current.year, date__month=current.month)
        # Goes through each signup for the family and calculates total hours for the month
        for day in signups:
            end = datetime.timedelta(hours=day.end_time.hour,minutes=day.end_time.minute)
            start = datetime.timedelta(hours=day.start_time.hour,minutes=day.start_time.minute)
            total = total + (end - start)
        return total


    """ This functions return the required hours a family must complete (as an integer)
        in a few depending on how many children they have. 
        Return:
            It returns an int of the amount of hours the family must complete
        Param:
            requested_family: is the family that you want the number of children for.
                It must be a single Family object (from user.models)
    """
    def required_hours(self, requested_family):
        children = (Child.objects.filter(family__familyID = requested_family.familyID).count())
        return (2.5 if children < 2 else 5)




class AdminStats(generic.ListView):
    template_name = "admin_stats.html"
    model = Signup


    def __init__(self):
        pass












