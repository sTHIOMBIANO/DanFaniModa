# Generated by Django 4.2.2 on 2023-06-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_produit_similaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='type',
            field=models.CharField(default='pagne'),
        ),
    ]