# Generated by Django 3.0.6 on 2020-07-25 18:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('meeting_type', models.CharField(choices=[('SU', 'Status Update'), ('IS', 'Information Sharing'), ('DM', 'Decision Making'), ('PS', 'Problem Solving'), ('IN', 'Innovation'), ('TB', 'Team Building')], default='SU', max_length=2)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('duration', models.IntegerField(default=1)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room')),
            ],
        ),
    ]