# Generated by Django 4.2.2 on 2023-06-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('do_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
