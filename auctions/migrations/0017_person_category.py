# Generated by Django 3.0.7 on 2020-11-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20201103_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.Category'),
        ),
    ]
