# Generated by Django 4.2.2 on 2023-06-29 15:36

import Appointment.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(validators=[Appointment.models.validate_date_range])),
                ('start_time', models.TimeField(validators=[Appointment.models.validate_time_range])),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(blank=True, choices=[('A', 'AVAILABLE'), ('R', 'RESERVED')], default='A', max_length=1, null=True)),
                ('duration', models.PositiveIntegerField(choices=[(30, '30 minutes'), (45, '45 minutes'), (60, '1 hour'), (90, '1.5 hours'), (120, '2 hours')])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='Doctor.doctor')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]
