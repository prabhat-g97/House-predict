# Generated by Django 2.0.7 on 2021-01-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210122_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.TextField(),
        ),
    ]
