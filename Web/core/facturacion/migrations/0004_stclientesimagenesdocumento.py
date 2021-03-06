# Generated by Django 3.0.6 on 2020-09-15 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_vtcomprobanteweb'),
    ]

    operations = [
        migrations.CreateModel(
            name='StClientesImagenesDocumento',
            fields=[
                ('fecha_transaccion', models.DateField(primary_key=True, serialize=False)),
                ('cod_cliente', models.CharField(blank=True, max_length=30, null=True)),
                ('empresa', models.IntegerField()),
                ('codigo_tipo_imagen_documento', models.IntegerField()),
                ('documento', models.BinaryField(blank=True, null=True)),
                ('adicionado_por', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_adicion', models.DateField(blank=True, null=True)),
                ('modificado_por', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
                ('anulado', models.CharField(max_length=1)),
                ('procesado', models.CharField(blank=True, max_length=2, null=True)),
                ('path_dir', models.CharField(blank=True, max_length=200, null=True)),
                ('documento1', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'st_clientes_imagenes_documento',
                'managed': False,
            },
        ),
    ]
