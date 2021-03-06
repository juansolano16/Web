# Generated by Django 3.0.6 on 2020-08-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_stproformacabeceratmp_stproformadetalletmp'),
    ]

    operations = [
        migrations.CreateModel(
            name='VtComprobanteWeb',
            fields=[
                ('empresa', models.IntegerField()),
                ('agencia', models.CharField(max_length=50)),
                ('cod_comprobante', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('tipo_comprobante', models.CharField(max_length=50)),
                ('comprobante_sri', models.CharField(blank=True, max_length=20, null=True)),
                ('cod_persona', models.CharField(max_length=14)),
                ('fecha', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=14)),
                ('nombre_persona', models.CharField(blank=True, max_length=80, null=True)),
                ('forma_pago', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'vt_comprobante_web',
                'managed': False,
            },
        ),
    ]
