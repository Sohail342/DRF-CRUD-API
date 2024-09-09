from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    # Get, Refresh and Verify Token for Authentication 
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/token/', TokenRefreshView.as_view()),
    
    
    path('list/', views.student_list, name='student-list'),
    path('list/<int:id>/', views.student_list, name='student-list'),
    path('create/', views.student_create, name='student-create'),
    path('update/<int:id>/', views.student_update, name='student-update'),
    path('destroy/<int:id>/', views.student_delete, name='student-destroy'),
]
