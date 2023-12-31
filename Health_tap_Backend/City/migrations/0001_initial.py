# Generated by Django 4.2.2 on 2023-07-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=255, unique=True)),
                ('name_en', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
