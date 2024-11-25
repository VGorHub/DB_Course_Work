# Generated by Django 4.2.16 on 2024-11-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_column='Full Name', max_length=255)),
                ('email', models.EmailField(db_column='Email', max_length=254, unique=True)),
                ('age', models.IntegerField(db_column='Age')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_column='Full Name', max_length=255)),
                ('years_of_experience', models.IntegerField(db_column='Years of Experience')),
                ('position', models.CharField(db_column='Position', max_length=255)),
                ('salary', models.DecimalField(db_column='Salary', decimal_places=2, max_digits=10)),
                ('age', models.IntegerField(db_column='Age')),
                ('photo', models.BinaryField(blank=True, db_column='Photo', null=True)),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'db_table': 'Employee',
            },
        ),
    ]