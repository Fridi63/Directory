from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'patronymic', 'employment_date', 'salary', 'paid_salary', 'level', 'position']
