# Generated by Django 2.2.7 on 2020-01-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200129_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='comics',
            name='comic_code',
            field=models.CharField(default='', max_length=100),
        ),
    ]
