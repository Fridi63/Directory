# Generated by Django 3.2.12 on 2022-03-25 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_alter_employee_employment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employment_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 25, 9, 4, 47, 372174)),
        ),
    ]
