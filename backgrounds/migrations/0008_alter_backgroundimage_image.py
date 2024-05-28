# Generated by Django 4.2.8 on 2024-05-28 18:01

import backgrounds.models
import backgrounds.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backgrounds', '0007_alter_backgroundimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundimage',
            name='image',
            field=models.ImageField(storage=backgrounds.storage.OverwriteStorage(), upload_to=backgrounds.models.profile_picture_path, verbose_name='Imagen'),
        ),
    ]