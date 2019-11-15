# Generated by Django 2.2.5 on 2019-11-15 23:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineShopperTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Administrative', models.IntegerField(default=0)),
                ('Administrative_Duration', models.IntegerField(default=0)),
                ('Informational', models.IntegerField(default=0)),
                ('Informational_Duration', models.FloatField(default=0)),
                ('ProductRelated', models.IntegerField(default=0)),
                ('ProductRelated_Duration', models.FloatField(default=0)),
                ('BounceRates', models.FloatField(default=0)),
                ('ExitRates', models.FloatField(default=0)),
                ('PageValues', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('Month', models.CharField(max_length=15)),
                ('OperatingSystems', models.IntegerField(validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(8)])),
                ('Browser', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(13)])),
                ('Region', models.IntegerField(validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(9)])),
                ('TrafficType', models.IntegerField(validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(20)])),
                ('Visitor_type', models.CharField(choices=[('Returning', 'Returning_Visitor'), ('New', 'New_Visitor'), ('Other', 'Other')], max_length=50)),
                ('Weekend', models.BooleanField()),
                ('Revenue', models.BooleanField()),
            ],
        ),
    ]