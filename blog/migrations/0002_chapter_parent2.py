# Generated by Django 3.0.8 on 2022-11-02 07:26

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='parent2',
            field=mptt.fields.TreeManyToManyField(blank=True, related_name='children_parent', to='blog.Chapter'),
        ),
    ]
