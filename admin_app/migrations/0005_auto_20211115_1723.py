# Generated by Django 3.2.7 on 2021-11-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_auto_20211115_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='checkin_time',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='checkout_time',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
