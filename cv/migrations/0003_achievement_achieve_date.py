# Generated by Django 2.2.4 on 2020-08-28 19:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_achievement_workexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='achieve_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
