# Generated by Django 2.2.1 on 2021-01-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]
