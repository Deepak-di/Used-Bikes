# Generated by Django 5.0.1 on 2024-03-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_bikes_model_object_bikes_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='ownership',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
