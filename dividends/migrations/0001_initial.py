# Generated by Django 2.1.5 on 2019-03-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dividend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('sector', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('cons_years', models.IntegerField()),
                ('ranking', models.IntegerField()),
                ('drip_fees', models.CharField(max_length=1, null=True)),
                ('spp_fees', models.CharField(max_length=1, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('div_yield', models.DecimalField(decimal_places=2, max_digits=4)),
                ('current_dividend', models.DecimalField(decimal_places=4, max_digits=6)),
                ('num_payouts', models.IntegerField()),
                ('annual_dividend', models.DecimalField(decimal_places=2, max_digits=5)),
                ('schedule', models.CharField(max_length=6)),
                ('previous_dividend', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ex_dividend_date', models.DateField()),
                ('payable_date', models.DateField()),
                ('mr_increase', models.DecimalField(decimal_places=3, max_digits=5)),
                ('dgr_1', models.DecimalField(decimal_places=3, max_digits=7)),
                ('dgr_3', models.DecimalField(decimal_places=3, max_digits=7)),
                ('dgr_5', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('dgr_10', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('ad_5_10', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('deg_5', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('eps', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('ttm_pe', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('fye', models.IntegerField()),
            ],
        ),
    ]
