# Generated by Django 4.2 on 2023-04-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectManagement', '0006_alter_project_info_project_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_info',
            name='project_file',
            field=models.FileField(upload_to='project_file/%Y/%m/%d/', verbose_name='脚本路径'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='limits',
            field=models.CharField(choices=[(1, '普通用户'), (2, '中级用户'), (3, '管理员'), (4, '超级管理员')], max_length=16, verbose_name='账号权限'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='status',
            field=models.CharField(choices=[(2, '失效'), (1, '正常')], max_length=16, verbose_name='状态'),
        ),
    ]
