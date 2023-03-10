# Generated by Django 2.0.3 on 2021-02-07 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_productwishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('unpublished', 'Unpublished'), ('moderated', 'Moderated')], default='published', max_length=30, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='productbasket',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Color', verbose_name='Color'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productbasket',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productbasket',
            name='price',
            field=models.PositiveIntegerField(default=1, verbose_name='Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productbasket',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Size', verbose_name='Size'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productbasket',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Basket', verbose_name='Basket'),
        ),
        migrations.AlterField(
            model_name='productbasket',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product'),
        ),
    ]
