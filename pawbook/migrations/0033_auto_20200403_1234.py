# Generated by Django 2.2.3 on 2020-04-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawbook', '0032_auto_20200403_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(storage='post_image/', upload_to='post_image/'),
        ),
    ]