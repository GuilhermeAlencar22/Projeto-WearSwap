# Generated by Django 5.0.4 on 2024-05-06 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wear_swaps', '0003_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='bio',
        ),
    ]
