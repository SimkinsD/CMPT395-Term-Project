from django.shortcuts import render
from django.views.generic import TemplateView

import calendar
import datetime

# Create your views here.
class WeeklyCalendarView(TemplateView):
  template_name = "calendar.html"
  WEEK_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday"
               , "Thursday", "Friday", "Saturday"]

  def __init__(self):
    self.week = self.getWeek()

    self.day_and_name = self.pairDayName()
    self.day_and_name = self.day_and_name[1:-1]

  def getWeek(self):
    """ Returns list of 7 datetime objects which represent the current week """
    date = datetime.datetime.now()
    month = calendar.Calendar(6).monthdatescalendar(date.year, date.month)
    for week in month:
      for day in week:
        if date.day == day.day:
          return week

  def pairDayName(self):
    day_name = []
    for i in range(len(self.week)):
      day_name.append((self.WEEK_DAYS[i], self.week[i]))
    return day_name