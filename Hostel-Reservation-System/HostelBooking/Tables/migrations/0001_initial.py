# Generated by Django 4.0 on 2023-03-12 15:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FLOOR',
            fields=[
                ('floor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('floor_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('brand_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ROOM',
            fields=[
                ('room_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room_no', models.IntegerField()),
                ('room_status', models.BooleanField(default='true')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tables.floor')),
            ],
        ),
    ]
