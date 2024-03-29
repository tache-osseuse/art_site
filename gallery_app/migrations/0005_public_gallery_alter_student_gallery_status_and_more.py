# Generated by Django 4.1 on 2023-05-07 21:35

from django.db import migrations, models
import django.db.models.deletion
import gallery_app.file_methods


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_admin_profile_first_name_and_more'),
        ('gallery_app', '0004_rename_img_teacher_picture_teacher_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Public_Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Название галереи')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Описание галереи')),
                ('code_name', models.CharField(blank=True, max_length=150, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher_profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='student_gallery',
            name='status',
            field=models.CharField(choices=[('PRIVATE', 'Закрытая'), ('INNER', 'Внутренняя'), ('PUBLIC', 'Открытая')], max_length=50, verbose_name='Видимость галереи'),
        ),
        migrations.CreateModel(
            name='Public_Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Название картины')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Описание картины')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации картины')),
                ('public_img', models.ImageField(upload_to=gallery_app.file_methods.get_public_pic_path)),
                ('public_gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery_app.public_gallery')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
