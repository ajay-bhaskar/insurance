# Generated by Django 4.0.2 on 2022-02-28 00:51

from django.db import migrations, models
import policy.models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0003_alter_insurancedata_date_of_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancedata',
            name='premium',
            field=models.IntegerField(validators=[policy.models.validate_premium], verbose_name='Premium'),
        ),
    ]
