# Generated by Django 5.0.4 on 2024-05-31 19:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wear_swaps', '0010_carrinho_itemcarrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='carrinho',
        ),
        migrations.AddField(
            model_name='itemcarrinho',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
