# Generated by Django 4.1 on 2022-08-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0002_remove_recipe_category_category_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
