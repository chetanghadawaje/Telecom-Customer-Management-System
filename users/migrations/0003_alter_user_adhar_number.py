# Generated by Django 4.2.11 on 2024-04-06 16:36

from django.db import migrations, models
import tcms.utils.models_utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='adhar_number',
            field=models.CharField(max_length=12, validators=[tcms.utils.models_utils.only_int, tcms.utils.models_utils.adhar_digit]),
        ),
    ]