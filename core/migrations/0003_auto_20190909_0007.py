# Generated by Django 2.2.5 on 2019-09-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_motherboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='slotRam',
            field=models.IntegerField(default=True),
        ),
    ]