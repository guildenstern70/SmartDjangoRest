# Generated by Django 3.1.5 on 2021-10-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartdjangorest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
