# Generated by Django 3.1.5 on 2021-01-24 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210124_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
    ]
