# Generated by Django 2.0.7 on 2019-07-23 15:19

from django.db import migrations, models
import django.db.models.deletion
import timetables.models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0002_auto_20190723_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetables.Day', verbose_name=timetables.models.Day)),
            ],
        ),
        migrations.RemoveField(
            model_name='timeslots',
            name='day',
        ),
        migrations.DeleteModel(
            name='TimeSlots',
        ),
    ]
