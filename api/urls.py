from django.urls import path
from api import views

urlpatterns = [
    path('studentapilist/', views.StudentList.as_view(), name='student-list'),
    path('studentapicreate/', views.StudentCreate.as_view(), name='student-create'),
    path('studentapiretreive/<int:pk>/', views.StudentRetreive.as_view(), name='student-retrieve'),
    path('studentapiupdate/<int:pk>/', views.StudentUpdate.as_view(), name='student-update'),
    path('studentapidestroy/<int:pk>/', views.StudentDestroy.as_view(), name='student-destroy'),
]
