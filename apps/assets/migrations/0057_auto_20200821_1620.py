# Generated by Django 2.2.13 on 2020-08-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0056_auto_20200816_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='assets_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='parent_key',
            field=models.CharField(db_index=True, default='', max_length=64, verbose_name='Parent key'),
        ),
    ]
