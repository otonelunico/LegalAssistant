# Generated by Django 2.0.1 on 2018-01-18 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Base', '0011_reunion_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reunion',
            name='url',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
