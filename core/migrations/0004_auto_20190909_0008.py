# Generated by Django 2.2.5 on 2019-09-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190909_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='slotRam',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='video',
            field=models.BooleanField(default=True),
        ),
    ]
