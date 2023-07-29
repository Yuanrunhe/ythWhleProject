# Generated by Django 4.2 on 2023-04-15 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectManagement', '0002_remove_projrct_info_path_projrct_info_project_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projrct_info',
            name='project_file',
            field=models.FileField(max_length=128, upload_to='project_file/', verbose_name='脚本路径'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='limits',
            field=models.CharField(choices=[(4, '超级管理员'), (3, '管理员'), (2, '中级用户'), (1, '普通用户')], max_length=16, verbose_name='账号权限'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='status',
            field=models.CharField(choices=[(1, '正常'), (2, '失效')], max_length=16, verbose_name='状态'),
        ),
    ]
