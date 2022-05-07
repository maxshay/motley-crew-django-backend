# Generated by Django 4.0.2 on 2022-05-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_slips', '0006_alter_routeslip_order_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routeslip',
            name='current_route_item_id',
        ),
        migrations.AddField(
            model_name='routeslip',
            name='current_route_item',
            field=models.UUIDField(null=True),
        ),
    ]
