# Generated by Django 4.2.2 on 2023-07-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_panier'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='slug',
            field=models.SlugField(default='', max_length=128, unique=True),
            preserve_default=False,
        ),
    ]