# Generated by Django 2.0.7 on 2019-11-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0011_periods_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periods',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='periods',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
