# Generated by Django 3.0.6 on 2020-07-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_rhpersonalturnos_vtturnos'),
    ]

    operations = [
        migrations.CreateModel(
            name='VtPersonalTurnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.IntegerField()),
                ('cedula', models.CharField(max_length=14)),
                ('empleado', models.CharField(blank=True, max_length=101, null=True)),
                ('agencia', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=200)),
                ('cod_turno', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'vt_personal_turnos',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='RhPersonalTurnos',
        ),
    ]
