# Generated by Django 2.2.3 on 2020-04-02 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pawbook', '0026_merge_20200402_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='petImage',
            field=models.ImageField(storage='D:\\pawbook_wad\\media/listing_image/', upload_to='listing_image'),
        ),
        migrations.AlterField(
            model_name='petpedia',
            name='picture',
            field=models.ImageField(blank=True, default=None, storage='D:\\pawbook_wad\\media/petPedia_image/', upload_to='petPedia_image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(storage='D:\\pawbook_wad\\media/post_image/', upload_to='post_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilePicture',
            field=models.ImageField(blank=True, default=None, storage='D:\\pawbook_wad\\media/profile_image/', upload_to='profile_image'),
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserPreference', to='pawbook.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserPreference', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'post', 'value')},
            },
        ),
    ]