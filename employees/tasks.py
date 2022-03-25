from config.celery import app
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Employee
# from django.db import connection
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
@shared_task()
def pay_salary():
    # with connection.cursor() as cursor:
    logger.info("1")
    # employees = Employee.objects.all()
    # logger.info("2")
    # for employee in employees:
    #     logger.info("3")
    #     employee.paid_salary += employee.salary
    #     employee.save()
