# Generated by Django 5.0.4 on 2024-05-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wear_swaps', '0005_itemadicionado_lojaitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
