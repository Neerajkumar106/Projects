# Generated by Django 4.0 on 2023-03-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0004_remove_req_room_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='req_room',
            name='room',
        ),
    ]
