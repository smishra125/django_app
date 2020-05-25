from django.contrib import admin
from .models import Employee

# Register your models here.
admin.site.register(Employee)


def __str__(self):
    return self.ename
