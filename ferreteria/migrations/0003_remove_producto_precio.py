# Generated by Django 5.0.6 on 2024-06-20 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0002_producto_descripcion_producto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
    ]
