# Generated by Django 4.0.2 on 2022-05-07 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('route_items', '0006_routeitem_form_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routeitem',
            name='form_field',
        ),
    ]
