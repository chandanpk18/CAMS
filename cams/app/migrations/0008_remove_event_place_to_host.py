# Generated by Django 5.0.2 on 2024-05-20 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_manager_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='place_to_host',
        ),
    ]
