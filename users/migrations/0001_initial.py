# Generated by Django 4.2.11 on 2024-04-06 09:25

from django.db import migrations, models
import tcms.utils.models_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('adhar_number', models.CharField(max_length=12, validators=[tcms.utils.models_utils.only_int])),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('mobile_number', models.CharField(max_length=10)),
            ],
        ),
    ]