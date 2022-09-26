from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display  =['id','First_name','Last_name','Phone','Email','Department']