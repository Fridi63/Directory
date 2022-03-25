from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils import Choices
import datetime as dt


class Level(models.IntegerChoices):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4


class Employee(AbstractUser):
    POSITION = Choices('director', 'supervisor', 'middle_manager', 'manager', 'developer')

    patronymic = models.CharField(max_length=50, null=True, blank=True)
    employment_date = models.DateField(default=dt.datetime.now())
    salary = models.FloatField(default=100)
    paid_salary = models.FloatField(default=100)
    position = models.CharField(choices=POSITION, default=POSITION.developer, max_length=20)
    level = models.IntegerField(choices=Level.choices, default=Level.FOUR)
    chief = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
