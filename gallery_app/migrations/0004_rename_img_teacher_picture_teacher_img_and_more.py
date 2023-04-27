# Generated by Django 4.1 on 2023-04-27 14:46

from django.db import migrations, models
import gallery_app.file_methods


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0003_student_picture_teacher_picture_delete_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_picture',
            old_name='img',
            new_name='teacher_img',
        ),
        migrations.RemoveField(
            model_name='student_picture',
            name='img',
        ),
        migrations.AddField(
            model_name='student_picture',
            name='student_img',
            field=models.ImageField(default=1, upload_to=gallery_app.file_methods.get_student_pic_path),
            preserve_default=False,
        ),
    ]
