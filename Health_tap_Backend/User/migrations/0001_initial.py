# Generated by Django 4.2.2 on 2023-06-25 21:46

import User.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Specialization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True, validators=[User.models.validate_date_of_birth])),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='EG', unique=True)),
                ('national_id', models.CharField(max_length=14, validators=[User.models.validate_egypt_national_id])),
                ('profileImgUrl', models.ImageField(blank=True, upload_to='profileImages/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profLicenseNo', models.CharField(max_length=6, validators=[User.models.validate_profLicenseNum])),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Specialization', to='Specialization.specialization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]