# Generated by Django 4.2.6 on 2023-11-18 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_entrepreneurprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepreneurprofile',
            name='UserId',
            field=models.IntegerField(default=100),
        ),
    ]
