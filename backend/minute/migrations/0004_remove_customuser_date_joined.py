# Generated by Django 5.1.2 on 2024-10-11 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minute', '0003_alter_customuser_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
    ]