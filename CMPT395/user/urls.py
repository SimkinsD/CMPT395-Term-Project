from django.urls import path
from . import views

urlpatterns = [
    path('registor/', views.Registor.as_view(), name='registor'),
    path('registor_teacher/', views.RegistorTeacher.as_view(), name='registor_teacher'),
    path('person/', views.AddPerson.as_view() , name='person'),
    path('view_family/', views.ViewFamily , name='view_family'),
]