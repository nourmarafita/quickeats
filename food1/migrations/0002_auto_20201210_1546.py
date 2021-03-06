# Generated by Django 3.1 on 2020-12-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bImage', models.URLField()),
            ],
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='pimage',
            new_name='pImage',
        ),
    ]
