# Generated by Django 3.1.1 on 2020-11-01 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='desc_prod',
            new_name='descripcion_producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='foto_prod',
            new_name='foto_producto',
        ),
    ]