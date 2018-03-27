from django.urls import path, include

from . import views

urlpatterns = [
    path('family/', views.FamilyStats.as_view(), name='family_stats'),
]