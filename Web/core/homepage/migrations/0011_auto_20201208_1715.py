# Generated by Django 3.0.6 on 2020-12-08 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('homepage', '0010_auto_20201208_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebarmenudet',
            name='id_group',
        ),
        migrations.AddField(
            model_name='sidebarmenu',
            name='id_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.Group'),
        ),
    ]