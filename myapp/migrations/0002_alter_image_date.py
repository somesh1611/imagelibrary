# Generated by Django 3.2.9 on 2021-11-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default='datetime.now – from datetime.now()'),
        ),
    ]
