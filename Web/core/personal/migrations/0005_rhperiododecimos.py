# Generated by Django 3.0.6 on 2020-07-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20200714_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='RhPeriodoDecimos',
            fields=[
                ('empresa', models.IntegerField()),
                ('periodo', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('fdesde', models.CharField(max_length=6)),
                ('fhasta', models.CharField(max_length=6)),
                ('tipo', models.CharField(max_length=10)),
                ('pregion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'rh_periodo_decimos',
                'managed': False,
            },
        ),
    ]
