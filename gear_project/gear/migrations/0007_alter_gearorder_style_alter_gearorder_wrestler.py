# Generated by Django 4.0.4 on 2022-05-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0006_alter_galleryphotoitem_galleryitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearorder',
            name='style',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gearorder',
            name='wrestler',
            field=models.CharField(max_length=100),
        ),
    ]
