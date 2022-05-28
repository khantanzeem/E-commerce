# Generated by Django 3.2.3 on 2021-10-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20211016_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='items_json',
            field=models.CharField(default=' ', max_length=5000),
        ),
        migrations.AddField(
            model_name='orderupdate',
            name='name',
            field=models.CharField(default=' ', max_length=90),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.CharField(max_length=1000),
        ),
    ]