# Generated by Django 3.1.5 on 2021-07-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myneighbour', '0007_auto_20210726_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]