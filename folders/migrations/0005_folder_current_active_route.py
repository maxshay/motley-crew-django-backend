# Generated by Django 4.0.2 on 2022-03-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0004_folder_color_folder_confidential_folder_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='current_active_route',
            field=models.IntegerField(null=True),
        ),
    ]
