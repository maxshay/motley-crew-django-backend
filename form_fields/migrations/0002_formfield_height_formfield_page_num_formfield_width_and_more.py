# Generated by Django 4.0.2 on 2022-05-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_fields', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='height',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formfield',
            name='page_num',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formfield',
            name='width',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formfield',
            name='xpos',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='formfield',
            name='ypos',
            field=models.SmallIntegerField(default=0),
        ),
    ]
