# Generated by Django 4.2.3 on 2023-07-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='expirationDate',
            field=models.DateField(),
        ),
    ]
