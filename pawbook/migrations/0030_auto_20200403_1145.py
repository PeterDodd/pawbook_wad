# Generated by Django 2.2.3 on 2020-04-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawbook', '0029_auto_20200403_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='petImage',
            field=models.ImageField(storage='listing_image/', upload_to='listing_image/'),
        ),
        migrations.AlterField(
            model_name='petpedia',
            name='picture',
            field=models.ImageField(blank=True, default=None, storage='petPedia_image/', upload_to='petPedia_image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(storage='post_image/', upload_to='post_image/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(blank=True, default=None, storage='profile_image/', upload_to='profile_image/'),
        ),
    ]
