from django.contrib import admin

# Register your models here.
from .models import Student, Department

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    search_fields = ('name','age', 'email')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'no_of_students')
    search_fields = ('name', 'faculty')
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Department,DepartmentAdmin)