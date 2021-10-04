# Generated by Django 3.2.7 on 2021-10-01 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depname', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default='1')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='members_personalinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('tel_no', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default='1')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default='1')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default='1')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin_app.members_personalinfo')),
            ],
        ),
        migrations.AddField(
            model_name='members_personalinfo',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.roles'),
        ),
        migrations.CreateModel(
            name='guest_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('tel_no', models.CharField(max_length=255, unique=True)),
                ('nid', models.CharField(max_length=255, unique=True)),
                ('visit_reason', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default='1')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='finance_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.CharField(max_length=255)),
                ('balance', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default='1')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin_app.members_personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_time', models.DateTimeField()),
                ('checkout_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default='1')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.guest_application')),
                ('member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.members_personalinfo')),
            ],
        ),
    ]
