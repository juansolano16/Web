# Generated by Django 3.0.6 on 2020-08-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_vtproductodetalle'),
    ]

    operations = [
        migrations.CreateModel(
            name='VtCaracteristicasProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristicas', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'vt_dist_prod_detalle',
                'managed': False,
            },
        ),
    ]
