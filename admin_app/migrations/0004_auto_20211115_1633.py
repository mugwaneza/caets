# Generated by Django 3.2.7 on 2021-11-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_alter_guest_application_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest_application',
            name='is_active',
        ),
        migrations.AddField(
            model_name='guest_application',
            name='status',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
