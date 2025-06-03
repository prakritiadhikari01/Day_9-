from django.urls import path
from . import views
urlpatterns = [
    path('students', views.student_api, name='student_api'),
    path('students/<int:pk>/', views.student_api, name='student_api'),
    path('departments/', views.department_api, name='department_api'),
]
