from django.contrib import admin
from .models import Student_Profile, Teacher_Profile, Study_Group
# Register your models here.

admin.site.register(Student_Profile)
admin.site.register(Teacher_Profile)
admin.site.register(Study_Group)
