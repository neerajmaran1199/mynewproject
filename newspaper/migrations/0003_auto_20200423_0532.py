# Generated by Django 2.2.2 on 2020-04-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='pics'),
        ),
    ]
