# Generated by Django 4.2.6 on 2024-01-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_investorproject_minimum_investment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorproject',
            name='allowed_risk',
            field=models.FloatField(verbose_name='Chance of Risk (%)'),
        ),
    ]
