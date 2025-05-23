# Generated by Django 5.2 on 2025-04-27 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_editorial_ciudad_alter_editorial_codigo_postal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
