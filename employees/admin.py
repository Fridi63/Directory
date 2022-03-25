from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

from .models import Employee, Level

from django.urls import reverse
from django.utils.html import format_html


@admin.action(description='Удалить информацию о выплатах')
def del_slary(modeladmin, request, queryset):
    queryset.update(paid_salary=0)


class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = (
            "username",
            "last_name",
            "first_name",
            "patronymic",
            "employment_date",
            "salary",
            "paid_salary",
            "position",
            "level",
            "chief",
        )

    def clean(self):
        position = self.cleaned_data.get('position')
        chief = self.cleaned_data.get('chief')
        print(f"{position=}")
        print(f"{chief=}")

        if position == "director" and chief != "":
            raise forms.ValidationError(
                "Director can not have chief")

        return self.cleaned_data


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ("last_name", "first_name", "patronymic", "salary", "paid_salary", "position", "view_chief_link", )
    readonly_fields = ('level',)

    def view_chief_link(self, obj):
        if obj.chief is None:
            return "-"
        url = reverse("admin:employees_employee_change", args=(obj.chief.id, ))

        return format_html('<a href="{}">{}</a>', url, f"{obj.chief.first_name} {obj.chief.last_name}")

    view_chief_link.short_description = "Chief"

    list_filter = ("position", "level")
    actions = [del_slary]

    def save_model(self, request, obj, form, change):

        # if obj.chief.level > obj.level or obj.position == "director":
        #     raise forms.ValidationError("Chief level must be higher than employee's")

        position_to_level = {
            "director": 0,
            "supervisor": 1,
            "middle_manager": 2,
            "manager": 3,
            "developer": 4
        }
        obj.level = position_to_level[obj.position]
        obj.save()
        super().save_model(request, obj, form, change)
