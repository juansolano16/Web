# Generated by Django 3.0.6 on 2020-09-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_stproductodetalleauvi_stproductoserieauvi_vt_producto_web_auvi_vtlistaprecioauvi'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodegaBajaj',
            fields=[
                ('cod_prov', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=70)),
                ('motor', models.CharField(max_length=30)),
                ('chasis', models.CharField(max_length=30)),
                ('anio', models.CharField(max_length=16)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('camvcpn', models.CharField(max_length=20)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('origen', models.CharField(blank=True, max_length=20, null=True)),
                ('locacion', models.CharField(max_length=12)),
                ('cilindraje', models.CharField(blank=True, max_length=10, null=True)),
                ('tonelaje', models.CharField(blank=True, max_length=10, null=True)),
                ('ruc', models.CharField(max_length=13)),
                ('descripcion', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'bodega_bajaj',
                'managed': False,
            },
        ),
    ]