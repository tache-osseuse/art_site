# Generated by Django 4.1 on 2023-04-20 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_admin_profile_first_name_and_more'),
        ('educational_app', '0020_alter_mark_test_test_attempt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mark_Test',
            new_name='Test_Mark',
        ),
    ]
