from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User.REQUIRED_FIELDS, on_delete=models.CASCADE)
    email_employee = models.EmailField()
    position_function = models.CharField()
    current_level = models.CharField()
    location = models.CharField(blank=True)
    direction = models.CharField()
    report_to = models.CharField()
    current_salary = models.PositiveIntegerField()
    current_project = models.TextField()
    birth_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    languages = models.TextField()
    level_of_languages = models.TextField()
    hours_worked = models.PositiveIntegerField()

