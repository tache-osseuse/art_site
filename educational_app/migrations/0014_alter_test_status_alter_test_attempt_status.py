# Generated by Django 4.1 on 2023-04-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_app', '0013_test_status_test_attempt_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='status',
            field=models.IntegerField(choices=[(1, 'PROCESS'), (2, 'DONE')], verbose_name='Статус теста'),
        ),
        migrations.AlterField(
            model_name='test_attempt',
            name='status',
            field=models.IntegerField(choices=[(1, 'CHECK'), (2, 'DENIED'), (3, 'ACCESS')], verbose_name='Статус решения теста'),
        ),
    ]
