# Generated by Django 4.2 on 2023-07-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newyunpan', '0005_filebook_file_type_alter_filebook_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='filebook',
            name='file_size',
            field=models.IntegerField(default=0, verbose_name='文件大小'),
        ),
    ]
