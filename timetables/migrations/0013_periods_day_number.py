# Generated by Django 2.0.7 on 2019-11-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0012_auto_20191104_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='periods',
            name='day_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]