# Generated by Django 4.1.2 on 2022-12-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_remove_tag_content_type_remove_tag_object_id'),
        ('recipes', '0004_recipe_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, default='', to='tag.tag'),
        ),
    ]
