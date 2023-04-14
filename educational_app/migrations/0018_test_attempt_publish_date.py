# Generated by Django 4.1 on 2023-04-14 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('educational_app', '0017_alter_test_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_attempt',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата попытки'),
            preserve_default=False,
        ),
    ]