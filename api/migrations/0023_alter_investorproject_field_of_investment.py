# Generated by Django 4.2.6 on 2024-01-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_investorproject_allowed_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorproject',
            name='field_of_investment',
            field=models.CharField(max_length=260, verbose_name='Project Name'),
        ),
    ]
