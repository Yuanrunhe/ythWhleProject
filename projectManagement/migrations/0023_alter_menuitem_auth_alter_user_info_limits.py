# Generated by Django 4.2 on 2023-07-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectManagement', '0022_alter_menuitem_auth_alter_user_info_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='auth',
            field=models.CharField(choices=[(2, '超级管理员'), (1, '普通用户'), (3, '全部')], default=3, max_length=16, verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='limits',
            field=models.CharField(choices=[(2, '超级管理员'), (1, '普通用户')], max_length=16, verbose_name='账号权限'),
        ),
    ]
