# Generated by Django 2.0.7 on 2019-06-18 13:20

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=accounts.models.User)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('surname', models.CharField(max_length=20, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('contact_name', models.CharField(max_length=20, null=True)),
                ('contact_number', models.IntegerField(null=True)),
                ('paid', models.NullBooleanField(default=False)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Club', verbose_name=users.models.Club)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Team'),
        ),
    ]
