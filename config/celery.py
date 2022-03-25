import os
from celery import Celery
# from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-3-hours': {
        'task': 'employees.tasks.pay_salary',
        'schedule': 20.0,
    },
}

app.autodiscover_tasks()




# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#       # Calls pay_salary every 3 hours
#     sender.add_periodic_task(60, pay_salary.s())
#
#
# @app.task
# def pay_salary():
#     employees = Employee.objects.all()
#     for employee in employees:
#         employee.paid_salary += employee.salary
