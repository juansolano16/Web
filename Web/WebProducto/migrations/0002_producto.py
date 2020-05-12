# Generated by Django 3.0.6 on 2020-05-11 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebProducto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('empresa', models.OneToOneField(db_column='empresa', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='WebProducto.Unidad')),
                ('cod_producto', models.CharField(max_length=40)),
                ('tipo_inventario', models.CharField(max_length=1)),
                ('cod_alterno', models.CharField(blank=True, max_length=14, null=True)),
                ('nombre', models.CharField(max_length=200)),
                ('cod_barra', models.CharField(blank=True, max_length=13, null=True)),
                ('useridc', models.CharField(max_length=3)),
                ('niv_cod_nivel', models.CharField(max_length=8)),
                ('niv_secuencia', models.CharField(max_length=6)),
                ('niv_cat_emp_empresa', models.CharField(max_length=2)),
                ('niv_cat_cod_categoria', models.CharField(max_length=10)),
                ('promedio', models.DecimalField(decimal_places=2, max_digits=12)),
                ('presentacion', models.CharField(blank=True, max_length=8, null=True)),
                ('volumen', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('grado', models.IntegerField(blank=True, null=True)),
                ('iva', models.CharField(max_length=1)),
                ('referencia', models.CharField(blank=True, max_length=200, null=True)),
                ('partida', models.CharField(blank=True, max_length=10, null=True)),
                ('minimo', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('maximo', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('costo', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('dolar', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('activo', models.CharField(max_length=1)),
                ('alcohol', models.CharField(blank=True, max_length=1, null=True)),
                ('cod_modelo', models.CharField(max_length=8)),
                ('cod_item', models.CharField(max_length=3)),
                ('es_fabricado', models.CharField(max_length=1)),
                ('cod_modelo_cat', models.CharField(blank=True, max_length=8, null=True)),
                ('cod_item_cat', models.CharField(blank=True, max_length=3, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('cantidad_i', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('serie', models.CharField(blank=True, max_length=1, null=True)),
                ('es_express', models.BooleanField(blank=True, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('cod_modelo_cat1', models.CharField(blank=True, max_length=8, null=True)),
                ('cod_item_cat1', models.CharField(blank=True, max_length=3, null=True)),
                ('bodega', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
    ]
