from django.contrib.auth.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.AddAccount.as_view(), name='account'),
    path('volunteer/', views.AddVolunteer.as_view(), name='volunteer'),
    path('family/', views.AddFamily.as_view() , name='family'),
    path('child/', views.AddChild.as_view(), name='child'),
    path('view_family/', views.ViewFamily.as_view() , name='view_family'),
    path('view_volunteer/', views.ViewVolunteer.as_view() , name='view_volunteer'),
    path('view_child/', views.ViewChild.as_view() , name='view_child'),
    path('edit_user/', views.UpdateUser.as_view(), name='update_user'),

    path('password_change', password_change, name='password_change'),
    path('password_change/done/', password_change_done, name='password_change_done'),
    path('password_change', password_change, name='password_change'),
    path('password_change/done/', password_change_done, name='password_change_done'),

    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/', password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),
]