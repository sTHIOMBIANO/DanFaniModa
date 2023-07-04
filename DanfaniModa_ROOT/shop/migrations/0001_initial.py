# Generated by Django 4.2.2 on 2023-06-24 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date_ajout', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=500)),
                ('prix', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='static/images')),
                ('date_ajout', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categorie')),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
    ]
