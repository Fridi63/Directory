from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import status

from .models import Employee
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSeniorStaff


class EmployeeListView(APIView):

    permission_classes = (IsAuthenticated, IsSeniorStaff, )

    def get(self, request):
        params = request.query_params
        if 'level' in params:
            employees = Employee.objects.filter(level=int(params['level']))
        else:
            employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees, many=True)

        print(request.query_params)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
