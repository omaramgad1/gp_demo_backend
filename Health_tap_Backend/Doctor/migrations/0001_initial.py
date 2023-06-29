# Generated by Django 4.2.2 on 2023-06-29 00:44

import Doctor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '__first__'),
        ('District', '0002_initial'),
        ('Specialization', '0001_initial'),
        ('City', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_doctor', models.BooleanField(default=True)),
                ('profLicenseNo', models.CharField(max_length=6, validators=[Doctor.models.validate_profLicenseNum])),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctorsByCity', to='City.city')),
                ('district', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctorsByDistrict', to='District.district')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Specialization', to='Specialization.specialization')),
            ],
            options={
                'abstract': False,
            },
            bases=('User.user',),
        ),
    ]
