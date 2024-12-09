# Generated by Django 4.2.16 on 2024-11-29 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20241127_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('employee', 'Employee')], db_column='Role', default='user', max_length=10),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
