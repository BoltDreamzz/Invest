# Generated by Django 5.0.6 on 2024-06-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_property_investment'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rating',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]