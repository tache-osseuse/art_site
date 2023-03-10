from django.db import models
from django.contrib.auth.models import User

class Study_Group(models.Model):
    number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'Группа {self.number}'

class Base_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30, blank=True)

    class Meta:
        abstract = True

class Teacher_Profile(Base_Profile):
    def __str__(self):
        return f'Преподаватель {self.last_name} {self.first_name}'

class Student_Profile(Base_Profile):
    group = models.ForeignKey(Study_Group, null=True, on_delete=models.SET_NULL) # вопрос, как быть с удалением групп и переопределением

    def __str__(self):
        return f'Студент {self.last_name} {self.first_name}'