# Generated by Django 4.0.4 on 2022-05-10 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0004_gearorder_haspaid_gearorder_iscomplete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryitem',
            name='photoUrl',
        ),
        migrations.CreateModel(
            name='GalleryPhotoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoName', models.CharField(max_length=100)),
                ('photoUrl', models.URLField()),
                ('galleryItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_photo_item', to='gear.galleryitem')),
            ],
        ),
    ]