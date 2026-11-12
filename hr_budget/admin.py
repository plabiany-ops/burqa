from django.contrib import admin
from .models import BudgetExpense, Department, Employee, Position


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'department', 'base_salary')
    list_filter = ('department', 'level')
    search_fields = ('title',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'position', 'contract_type', 'salary', 'status', 'vacation_month', 'vacation_days')
    list_filter = ('status', 'contract_type', 'department', 'night_shift', 'hazard')
    search_fields = ('name', 'cpf', 'email')
    fieldsets = (
        ('Dados pessoais', {'fields': ('name', 'cpf', 'email', 'department', 'position')}),
        ('Contrato', {'fields': ('contract_type', 'salary', 'benefits_cost', 'hire_date', 'status')}),
        ('Férias e adicionais', {'fields': ('vacation_month', 'vacation_days', 'vacation_abono_days', 'dependents', 'night_shift', 'hazard', 'commission_pct')}),
    )


@admin.register(BudgetExpense)
class BudgetExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'department', 'amount', 'month', 'year')
    list_filter = ('category', 'department', 'year')
    search_fields = ('category', 'description')
