# Generated by Django 4.0.2 on 2022-03-11 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('route_slips', '0002_routeslip_is_archived_alter_routeslip_current_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeslip',
            name='owner',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
