# Generated by Django 4.0.2 on 2022-05-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_fields', '0002_formfield_height_formfield_page_num_formfield_width_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='dimensions',
        ),
        migrations.AddField(
            model_name='formfield',
            name='form_type',
            field=models.CharField(default='sign', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='height',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page_num',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='width',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='xpos',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='ypos',
            field=models.SmallIntegerField(),
        ),
    ]