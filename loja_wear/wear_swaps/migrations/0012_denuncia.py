# Generated by Django 5.0.4 on 2024-06-01 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wear_swaps', '0011_remove_itemcarrinho_carrinho_itemcarrinho_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wear_swaps.produto')),
            ],
        ),
    ]