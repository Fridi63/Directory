from django.urls import path, include
from .views import EmployeeListView

urlpatterns = [
    path('', EmployeeListView.as_view()),
]
