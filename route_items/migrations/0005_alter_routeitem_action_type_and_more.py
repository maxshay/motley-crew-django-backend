# Generated by Django 4.0.2 on 2022-05-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_items', '0004_routeitem_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routeitem',
            name='action_type',
            field=models.CharField(choices=[('VIEW', 'view'), ('SIGN', 'sign'), ('OTHER', 'other')], max_length=8),
        ),
        migrations.AlterField(
            model_name='routeitem',
            name='completed_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='routeitem',
            name='order_num',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
