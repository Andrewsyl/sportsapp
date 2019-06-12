# Generated by Django 2.0.7 on 2019-06-12 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='user',
            field=models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
