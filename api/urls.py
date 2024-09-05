from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
         path('studentapilist/', views.StudentList.as_view()),
         path('studentapicreate/', views.StudentCreate.as_view()),
         path('studentapiretreive/<int:pk>/', views.StudentRetreive.as_view()),
         path('studentapiupdate/<int:pk>/', views.StudentUpdate.as_view()),
         path('studentapidestroy/<int:pk>/', views.StudentDestroy.as_view()),

]