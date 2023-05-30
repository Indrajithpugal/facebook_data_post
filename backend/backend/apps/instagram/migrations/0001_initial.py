# Generated by Django 3.2.14 on 2023-05-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_user_name', models.CharField(blank=True, default=None, max_length=2000, null=True)),
                ('insta_user_id', models.IntegerField(blank=True, default=None, null=True)),
                ('number_of_posts', models.FileField(blank=True, default=None, null=True, upload_to='insta_posts')),
                ('followers_count', models.IntegerField(blank=True, default=None, null=True)),
                ('following_count', models.IntegerField(blank=True, default=None, null=True)),
                ('biography', models.CharField(blank=True, default=None, max_length=2000, null=True)),
                ('external_url', models.CharField(blank=True, default=None, max_length=2000, null=True)),
            ],
        ),
    ]
