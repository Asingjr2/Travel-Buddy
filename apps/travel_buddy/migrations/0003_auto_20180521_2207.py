# Generated by Django 2.0.5 on 2018-05-21 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy', '0002_auto_20180521_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='destinations',
        ),
        migrations.AddField(
            model_name='destination',
            name='planner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_dest', to='travel_buddy.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='users_on_trip',
            field=models.ManyToManyField(related_name='destinations', to='travel_buddy.User'),
        ),
    ]
