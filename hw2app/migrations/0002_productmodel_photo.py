# Generated by Django 5.0.1 on 2024-02-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='photo',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='product_photos/'),
        ),
    ]