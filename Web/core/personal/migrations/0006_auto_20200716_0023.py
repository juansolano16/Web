# Generated by Django 3.0.6 on 2020-07-16 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_rhperiododecimos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rhperiododecimos',
            options={'managed': False, 'ordering': ['-periodo']},
        ),
        migrations.AlterModelTable(
            name='rhperiododecimos',
            table='vt_periodo_decimos',
        ),
    ]