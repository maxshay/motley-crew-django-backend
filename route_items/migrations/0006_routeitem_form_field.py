# Generated by Django 4.0.2 on 2022-05-07 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_fields', '0003_remove_formfield_dimensions_formfield_form_type_and_more'),
        ('route_items', '0005_alter_routeitem_action_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeitem',
            name='form_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form_fields.formfield'),
        ),
    ]
