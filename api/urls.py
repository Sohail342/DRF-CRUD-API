from .views import student_api, students_api
from django.urls import path


urlpatterns = [
    path('students/', students_api, name='students'),
    path('student/<int:id>/', student_api, name='student'),
]
