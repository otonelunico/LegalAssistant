# Generated by Django 2.0.1 on 2018-01-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Base', '0005_auto_20180113_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentacion',
            name='rut',
            field=models.CharField(default='1', max_length=10),
            preserve_default=False,
        ),
    ]
