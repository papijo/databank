# Generated by Django 3.2.3 on 2021-07-29 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NasDB', '0002_alter_nasorganisation_stage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nasorganisation',
            options={'ordering': ['name', 'id'], 'permissions': (('can_edit', 'Set NasOrganisation for Editing'),)},
        ),
    ]
