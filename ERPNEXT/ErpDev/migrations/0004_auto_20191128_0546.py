# Generated by Django 2.2.5 on 2019-11-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ErpDev', '0003_auto_20191126_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listtodo',
            name='created',
            field=models.DateField(default='2019-11-28'),
        ),
        migrations.AlterField(
            model_name='listtodo',
            name='due_date',
            field=models.DateField(default='2019-11-28'),
        ),
    ]
