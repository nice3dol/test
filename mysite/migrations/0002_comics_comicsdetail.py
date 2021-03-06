# Generated by Django 2.2.7 on 2019-12-05 13:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('author', models.CharField(default='', max_length=20)),
                ('catches', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ComicsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.IntegerField(default=1)),
                ('pub_datetime', models.DateField(default=django.utils.timezone.now)),
                ('comic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Comics')),
            ],
        ),
    ]
