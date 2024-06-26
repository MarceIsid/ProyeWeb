# Generated by Django 5.0.6 on 2024-06-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0007_alter_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo electrónico')),
                ('tipo_consulta', models.IntegerField(choices=[(0, 'consulta'), (1, 'reclamo'), (2, 'sugerencia'), (3, 'felicitaciones')])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
