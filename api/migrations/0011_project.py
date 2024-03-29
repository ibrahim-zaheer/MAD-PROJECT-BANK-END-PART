# Generated by Django 4.2.6 on 2023-11-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_entrepreneurprofile_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('field', models.CharField(max_length=100, verbose_name='Field')),
                ('minimum_investment', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Minimum Investment (USD)')),
                ('guaranteed_profit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Guaranteed Profit (USD)')),
                ('chance_of_risk', models.FloatField(verbose_name='Chance of Risk (%)')),
                ('description', models.TextField(verbose_name='Project Description')),
                ('time_scale', models.CharField(max_length=50, verbose_name='Time Scale')),
            ],
        ),
    ]
