# Generated by Django 3.1 on 2020-12-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0003_auto_20201214_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burger',
            name='priceL',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='burger',
            name='priceM',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='priceL',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='priceM',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
