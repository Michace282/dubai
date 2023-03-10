# Generated by Django 2.0.3 on 2022-08-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_product_pricesale'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTypeSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('product_type', models.CharField(choices=[('ladies', 'Ladies'), ('mens', 'Mens'), ('accessories', 'Accessories'), ('dance_shoes', 'Dance shoes'),('body', 'Body'), ('blouses', 'Blouses'), ('skirts', 'Skirts'), ('dresses', 'Dresses'), ('trousers', 'Trousers'), ('jumpsuits', 'Jumpsuits'), ('tops', 'Tops'), ('shorts', 'Shorts'),('trousers', 'Trousers'), ('waistcoasts', 'Waistcoasts'), ('shirts', 'Shirts'), ('t_shirts', 'T-shirts'), ('shoe_accessories', 'Shoe accessories'), ('bags', 'Bags'), ('ladies_accessories', 'Ladies accessories'), ('t_shirts', 'T-shirts'), ('ladies', 'Ladies'), ('mens', 'Mens')], max_length=30, verbose_name='Product type')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
