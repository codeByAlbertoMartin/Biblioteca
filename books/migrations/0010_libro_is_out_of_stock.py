# Generated by Django 5.2 on 2025-05-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_libro_descripcion_en_libro_descripcion_es_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='is_out_of_stock',
            field=models.BooleanField(default=False, verbose_name='Esta fuera de stock'),
        ),
    ]
