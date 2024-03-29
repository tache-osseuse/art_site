# Generated by Django 4.1 on 2023-04-16 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_admin_profile_first_name_and_more'),
        ('educational_app', '0018_test_attempt_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField()),
                ('max_points', models.PositiveIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student_profile', verbose_name='Студент')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educational_app.test', verbose_name='Тест')),
                ('test_attempt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='educational_app.test_attempt', verbose_name='Попытка выполнения теста')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
