# Generated by Django 4.2.6 on 2023-10-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_employees_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='phone',
            field=models.CharField(default='2395073221', max_length=50),
        ),
    ]
