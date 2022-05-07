# Generated by Django 4.0.2 on 2022-05-06 03:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_slips', '0007_remove_routeslip_current_route_item_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeslip',
            name='route_items_queue',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), default=list, size=None),
        ),
    ]
