# Generated by Django 2.0.3 on 2021-02-06 09:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0013_auto_20210205_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('status', models.CharField(choices=[('published', 'Published'), ('unpublished', 'Unpublished'), ('moderated', 'Moderated')], default='published', max_length=30, verbose_name='Status')),
                ('name_product', models.CharField(max_length=30, verbose_name='Name product')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '1110x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'ordering': ('published',),
            },
        ),
    ]
