# Generated by Django 4.2.6 on 2024-01-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_investorproject_minimum_investment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorproject',
            name='minimum_investment',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Minimum Investment (USD)'),
        ),
        migrations.AlterField(
            model_name='investorproject',
            name='minimum_profit',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Guaranteed Profit (USD)'),
        ),
        migrations.AlterField(
            model_name='investorproject',
            name='years_of_investment',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Field'),
        ),
    ]
