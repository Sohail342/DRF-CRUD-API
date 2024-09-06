from django.urls import path
from api import views

urlpatterns = [
    path('list/', views.student_list, name='student-list'),
    path('list/<int:id>/', views.student_list, name='student-list'),
    path('create/', views.student_create, name='student-create'),
    path('update/<int:id>/', views.student_update, name='student-update'),
    path('destroy/<int:id>/', views.student_delete, name='student-destroy'),
]
