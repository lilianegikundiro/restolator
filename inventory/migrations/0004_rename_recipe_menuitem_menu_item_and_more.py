# Generated by Django 4.2 on 2023-04-30 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_menuitem_recipe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='recipe',
            new_name='menu_item',
        ),
        migrations.RenameField(
            model_name='reciperequirement',
            old_name='menu_item',
            new_name='recipe',
        ),
    ]
