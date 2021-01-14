# Generated by Django 3.0.6 on 2021-01-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0011_auto_20201209_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='RhDepartamentos',
            fields=[
                ('cod_departamento', models.IntegerField(primary_key=True, serialize=False)),
                ('empresa', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('adicionado_por', models.CharField(max_length=30)),
                ('fecha_adicion', models.DateField()),
                ('modificado_por', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rh_departamentos',
                'managed': False,
            },
        ),
    ]