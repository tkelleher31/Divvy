# Generated by Django 2.1.5 on 2019-03-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dividend',
            name='mr_increase',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]