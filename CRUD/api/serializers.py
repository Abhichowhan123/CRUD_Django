from dataclasses import field
from rest_framework import serializers
from .models import*

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','First_name','Last_name','Phone','Email','Department']