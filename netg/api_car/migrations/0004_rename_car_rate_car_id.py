# Generated by Django 3.2.5 on 2021-07-19 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_car', '0003_auto_20210719_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='car',
            new_name='car_id',
        ),
    ]
