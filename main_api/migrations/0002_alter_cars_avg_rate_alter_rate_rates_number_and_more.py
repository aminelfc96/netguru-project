# Generated by Django 4.0.1 on 2022-01-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='avg_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rate',
            name='rates_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rate',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rate',
            name='sum_rate',
            field=models.IntegerField(),
        ),
    ]
