# Generated by Django 4.2 on 2023-04-21 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectManagement', '0007_alter_project_info_project_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='limits',
            field=models.CharField(choices=[(1, '普通用户'), (2, '超级管理员')], max_length=16, verbose_name='账号权限'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='status',
            field=models.CharField(choices=[(1, '正常'), (2, '失效')], max_length=16, verbose_name='状态'),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, null=True)),
                ('auth', models.CharField(choices=[(1, '普通用户'), (2, '超级管理员'), (3, '全部')], default=3, max_length=16, verbose_name='权限')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='projectManagement.menuitem')),
            ],
            options={
                'verbose_name': '菜单',
                'db_table': 'MenuItem',
            },
        ),
    ]
