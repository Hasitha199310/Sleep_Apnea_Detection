# Generated by Django 2.0 on 2018-05-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_remove_devices_connected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='last_connected',
            field=models.DateTimeField(),
        ),
    ]
