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
    self.date_and_name = self.pair_date_name(self.WEEK_DAYS, self.get_week())
    self.date_and_name = self.date_and_name[1:-1] # Trim week to Monday-Friday

  def get_week(self):
    """ Returns the current week represented by datetime objects
        Pre: None
        Post: None
        Parameters: None
        Return: List of 7 datetime objects representing the current week
    """
    date = datetime.datetime.now()
    # Get this month's calendar with the first day of the week as Sunday
    #   hence calendar.Calendar(6)
    month = calendar.Calendar(6).monthdatescalendar(date.year, date.month)
    for week in month:
      for day in week:
        if date.day == day.day:
          return week

  def pair_date_name(self, week_days, dates):
    """ Creates and returns list of tuples (string weekday, datetime date)
        Pre: week_days and dates are populated & ordered lists of strings and
          datetimes
        Post: None
        Param: week_days: Ordered list of string week day names
          e.g. ("Sunday", "Monday", etc.);
          dates: Ordered list of datetime objects;
          week_days and dates should be parallel
            (i.e. The first day in week_days should correspond to the first
            day in dates)
        Return: List of tuples of paired day names and datetimes
    """
    day_name = []
    for i in range(len(dates)):
      day_name.append((week_days[i], dates[i]))
    return day_name