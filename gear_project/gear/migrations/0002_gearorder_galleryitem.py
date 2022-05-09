# Generated by Django 4.0.4 on 2022-05-09 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GearOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gear_orders', to='gear.style')),
                ('wrestler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gear_orders', to='gear.wrestler')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=100)),
                ('photoUrl', models.CharField(max_length=300)),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_items', to='gear.style')),
                ('wrestler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_items', to='gear.wrestler')),
            ],
        ),
    ]
