# Generated by Django 3.1.1 on 2020-11-27 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20201101_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
