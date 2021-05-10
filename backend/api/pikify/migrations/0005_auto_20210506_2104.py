# Generated by Django 3.2 on 2021-05-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pikify', '0004_auto_20210505_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pikifyuser',
            name='profileImageUrl',
        ),
        migrations.AddField(
            model_name='pikifyuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
