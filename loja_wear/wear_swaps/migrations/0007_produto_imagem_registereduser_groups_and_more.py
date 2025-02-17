# Generated by Django 5.0.4 on 2024-05-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('wear_swaps', '0006_item_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='foto/default.jpg', upload_to='foto/'),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='item',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto/'),
        ),
        migrations.AlterField(
            model_name='itemadicionado',
            name='imagem',
            field=models.ImageField(upload_to='foto/'),
        ),
        migrations.AlterField(
            model_name='lojaitem',
            name='imagem',
            field=models.ImageField(upload_to='foto/'),
        ),
    ]
