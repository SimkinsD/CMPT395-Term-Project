from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.WeeklyCalendarView.as_view(), name='weeklyCalendar'),
]
