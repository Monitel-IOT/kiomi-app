# Generated by Django 3.2.7 on 2021-09-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210924_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='flavor',
        ),
        migrations.AddField(
            model_name='product',
            name='partsOfProduct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.partsofproduct', verbose_name='Parte del producto'),
        ),
        migrations.AlterField(
            model_name='partsofproduct',
            name='flavor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.flavor'),
        ),
    ]
