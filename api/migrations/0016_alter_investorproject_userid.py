# Generated by Django 4.2.6 on 2023-11-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_investorproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorproject',
            name='UserId',
            field=models.IntegerField(),
        ),
    ]
