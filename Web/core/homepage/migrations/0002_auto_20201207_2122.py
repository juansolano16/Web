# Generated by Django 3.0.6 on 2020-12-08 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sidebarmenu',
            options={'ordering': ['id'], 'verbose_name': 'Menu'},
        ),
    ]
