# Generated by Django 2.0.3 on 2021-02-05 15:37

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20210204_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.ImageField(blank=True, help_text='If an image is uploaded, it will be displayed in colors.', null=True, upload_to='', verbose_name='Image(64x64)'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='color',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Description'),
        ),
    ]
