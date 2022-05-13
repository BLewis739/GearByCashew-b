# Generated by Django 4.0.4 on 2022-05-12 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0007_alter_gearorder_style_alter_gearorder_wrestler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gearorder',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gear_orders', to='gear.style'),
        ),
        migrations.AlterField(
            model_name='gearorder',
            name='wrestler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gear_orders', to='gear.wrestler'),
        ),
    ]