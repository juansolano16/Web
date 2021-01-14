# Generated by Django 3.0.6 on 2020-08-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VtComprobante',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('emisor_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('tipodoc', models.CharField(db_column='tipoDoc', max_length=255)),
                ('fechaemision', models.DateField(db_column='fechaEmision')),
                ('fechaautorizacion', models.DateTimeField(db_column='fechaAutorizacion')),
                ('nodocumento', models.CharField(db_column='noDocumento', max_length=255)),
                ('claveacceso', models.CharField(db_column='claveAcceso', max_length=255)),
                ('numautorizacion', models.CharField(db_column='numAutorizacion', max_length=255)),
                ('dirxml', models.CharField(db_column='dirXML', max_length=255)),
                ('dirpdf', models.CharField(db_column='dirPDF', max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('mensaje', models.CharField(max_length=255)),
                ('informacionadicional', models.CharField(db_column='informacionAdicional', max_length=255)),
                ('user_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vt_comprobante',
                'managed': False,
            },
        ),
    ]