# Generated by Django 3.0.6 on 2020-12-08 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20201207_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebarmenudet',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.sidebarMenuDet'),
        ),
    ]