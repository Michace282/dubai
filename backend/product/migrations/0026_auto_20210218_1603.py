# Generated by Django 2.0.3 on 2021-02-18 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20210218_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_chart',
            field=models.ForeignKey(help_text='If you change the size table, the old dimensions will be deleted.', on_delete=django.db.models.deletion.CASCADE, to='product.SizeChart', verbose_name='Size Chart'),
        ),
    ]
