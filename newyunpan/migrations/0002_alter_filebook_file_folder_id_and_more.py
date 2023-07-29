# Generated by Django 4.2 on 2023-07-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newyunpan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebook',
            name='file_folder_id',
            field=models.ForeignKey(default=0, on_delete=models.SET(0), to='newyunpan.folderbook', verbose_name='关联文件夹'),
        ),
        migrations.AlterField(
            model_name='filebook',
            name='file_user_id',
            field=models.ForeignKey(default=0, on_delete=models.SET(0), to='newyunpan.newuserinfo', verbose_name='关联用户'),
        ),
        migrations.AlterField(
            model_name='folderbook',
            name='folder_fk_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='newyunpan.folderbook', verbose_name='文件上级关联'),
        ),
        migrations.AlterField(
            model_name='folderbook',
            name='folder_user_id',
            field=models.ForeignKey(default=0, on_delete=models.SET(0), to='newyunpan.newuserinfo', verbose_name='关联用户'),
        ),
        migrations.AlterField(
            model_name='newuserinfo',
            name='user_group_id',
            field=models.ForeignKey(default=0, on_delete=models.SET(0), to='newyunpan.usergroup', verbose_name='关联组'),
        ),
    ]
