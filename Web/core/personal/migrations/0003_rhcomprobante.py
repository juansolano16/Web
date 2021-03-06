# Generated by Django 3.0.6 on 2020-07-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_vtpersonal'),
    ]

    operations = [
        migrations.CreateModel(
            name='RhComprobante',
            fields=[
                ('tipo_comprobante', models.CharField(max_length=2)),
                ('cod_comprobante', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre_persona', models.CharField(blank=True, max_length=40, null=True)),
                ('fecha', models.DateField()),
                ('cod_agente', models.CharField(blank=True, max_length=14, null=True)),
                ('diastrabajados', models.DecimalField(decimal_places=2, max_digits=6)),
                ('totalingresos', models.DecimalField(decimal_places=2, max_digits=14)),
                ('totalegresos', models.DecimalField(decimal_places=2, max_digits=14)),
                ('totalrol', models.DecimalField(decimal_places=2, max_digits=14)),
                ('observaciones', models.CharField(blank=True, max_length=2000, null=True)),
                ('anulado', models.CharField(blank=True, max_length=1, null=True)),
                ('cod_liquidacion', models.CharField(max_length=9)),
                ('useridc', models.CharField(max_length=3)),
                ('aud_fecha', models.DateField(blank=True, null=True)),
                ('aud_usuario', models.CharField(blank=True, max_length=30, null=True)),
                ('aud_terminal', models.CharField(blank=True, max_length=50, null=True)),
                ('estado_grabado', models.CharField(blank=True, max_length=1, null=True)),
                ('estado_contabilizado', models.CharField(blank=True, max_length=1, null=True)),
                ('cod_agencia', models.IntegerField()),
                ('forma_pago', models.CharField(blank=True, max_length=3, null=True)),
                ('cod_opago', models.CharField(blank=True, max_length=9, null=True)),
                ('idsec', models.FloatField()),
                ('diasvacaciones', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'db_table': 'rh_comprobante',
                'managed': False,
            },
        ),
    ]
