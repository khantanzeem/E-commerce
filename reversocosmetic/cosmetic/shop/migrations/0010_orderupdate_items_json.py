# Generated by Django 3.2.3 on 2021-10-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orderupdate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
