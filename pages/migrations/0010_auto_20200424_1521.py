# Generated by Django 3.0.2 on 2020-04-24 15:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_member_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchfield',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default='html default'),
        ),
    ]