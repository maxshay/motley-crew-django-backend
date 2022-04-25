# Generated by Django 4.0.2 on 2022-03-27 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route_slips', '0004_rename_current_id_routeslip_current_route_item_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('action_type', models.CharField(choices=[('view', 'View'), ('sign', 'Sign'), ('other', 'Other')], default='view', max_length=8)),
                ('order_num', models.SmallIntegerField(null=True)),
                ('complete', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=255, null=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('route_slip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='route_slips.routeslip')),
            ],
        ),
    ]