# Generated by Django 3.1.7 on 2021-04-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
