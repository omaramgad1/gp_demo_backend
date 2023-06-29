# Generated by Django 4.2.2 on 2023-06-29 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('District', '0002_initial'),
        ('City', '0002_initial'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorsByCity', to='City.city'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorsByDistrict', to='District.district'),
        ),
    ]
