# Generated by Django 3.0.6 on 2020-12-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_bodegadaytona'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmpImagen',
            fields=[
                ('id', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=9, null=True)),
                ('archivo', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tmp_imagen',
                'managed': False,
            },
        ),
    ]