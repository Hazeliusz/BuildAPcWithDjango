# Generated by Django 3.2.3 on 2021-06-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210606_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='price',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cpu',
            name='price',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gpu',
            name='price',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='price',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='psu',
            name='price',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssd',
            name='price',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
    ]
