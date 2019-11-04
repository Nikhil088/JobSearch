# Generated by Django 2.2.4 on 2019-11-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191103_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]