# Generated by Django 5.0.7 on 2024-08-03 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_athlete_photo'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.school'),
        ),
    ]
