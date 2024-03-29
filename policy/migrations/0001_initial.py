# Generated by Django 4.0.2 on 2022-02-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insuranceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.IntegerField(verbose_name='Policy_id')),
                ('date_of_purchase', models.DateField(auto_now=True, verbose_name='Date of Purchase')),
                ('customer_id', models.IntegerField(verbose_name='Customer_id')),
                ('fuel', models.CharField(max_length=255, verbose_name='Fuel')),
                ('vehicle_segment', models.CharField(max_length=255, verbose_name='VEHICLE_SEGMENT')),
                ('premium', models.IntegerField(verbose_name='Premium')),
                ('bodily_injury_liability', models.IntegerField(verbose_name='bodily injury liability')),
                ('personal_injury_protection', models.IntegerField(verbose_name='personal injury protection')),
                ('property_damage_liability', models.IntegerField(verbose_name='property damage liability')),
                ('collision', models.IntegerField(verbose_name='collision')),
                ('comprehensive', models.IntegerField(verbose_name='comprehensive')),
                ('customer_gender', models.CharField(max_length=255, verbose_name='Customer_Gender')),
                ('customer_income_group', models.CharField(max_length=255, verbose_name='Customer_Income group')),
                ('customer_region', models.CharField(max_length=255, verbose_name='Customer_Region')),
                ('customer_marital_status', models.IntegerField(verbose_name='Customer_Marital_status')),
            ],
        ),
    ]
