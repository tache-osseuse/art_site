# Generated by Django 4.1 on 2023-03-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_app', '0006_course_code_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code_name',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]