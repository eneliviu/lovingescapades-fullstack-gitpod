# Generated by Django 5.1.4 on 2024-12-21 16:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dchoskzxj/image/upload/v1728654902/df0u5irtlmygzx4frtfe.webp', max_length=255, verbose_name='image'),
        ),
    ]
