# Generated by Django 3.2.3 on 2021-06-10 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TTA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='year',
        ),
        migrations.AddField(
            model_name='trainee',
            name='date_of_Program',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]