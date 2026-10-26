from django.contrib import admin

# Register your models here.
from .models import Department, Employee, Company

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ('id','name','email','age','salary','address','company', 'department')
    search_fields=('name','email')
    ordering = ('id',)
    list_filter = ('company',)
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display= ('id','name','email','branchNumber','location',)
    
    search_fields=('name','email')
    ordering = ('id',)  
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display= ('id','name','phone',)
    