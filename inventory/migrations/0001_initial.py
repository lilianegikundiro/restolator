# Generated by Django 4.2 on 2023-05-02 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=60, unique=True)),
                ('quantity', models.DecimalField(decimal_places=6, default=0, max_digits=12)),
                ('units', models.CharField(choices=[('g.', 'grams'), ('kg.', 'kilos'), ('L.', 'liters'), ('ml.', 'milliliters'), ('num', 'amount')], default='num', max_length=3)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_required', models.DecimalField(decimal_places=6, default=1, max_digits=12)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='inventory.ingredient')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menuitem', to='inventory.menuitem')),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='ingredients',
            field=models.ManyToManyField(through='inventory.RecipeRequirement', to='inventory.ingredient'),
        ),
    ]