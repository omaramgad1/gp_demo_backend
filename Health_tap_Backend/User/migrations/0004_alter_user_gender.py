# Generated by Django 4.2.2 on 2023-06-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('Male', 'M'), ('F', 'Female'), ('Female', 'F'), ('male', 'm'), ('m', 'male'), ('female', 'f'), ('f', 'female')]),
        ),
    ]