# Generated by Django 5.1 on 2024-08-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minute', '0002_rename_active_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Last Name'),
        ),
    ]
