# Generated by Django 2.1.1 on 2018-10-03 02:33

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article',
            field=markdownx.models.MarkdownxField(default=None),
        ),
    ]
