
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',views.EmployeeAPI.as_view()),
    path('employee/<int:pk>/',views.EmployeeAPI.as_view()),
]
