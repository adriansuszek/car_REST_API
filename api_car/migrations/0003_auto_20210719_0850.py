# Generated by Django 3.2.5 on 2021-07-19 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_car', '0002_auto_20210717_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_car.car'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
