# Generated by Django 4.0.4 on 2022-05-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervyu',
            name='link',
            field=models.URLField(),
        ),
    ]
