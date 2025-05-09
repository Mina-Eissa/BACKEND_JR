# Generated by Django 5.2 on 2025-05-01 12:26

import api.model.Article
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('authName', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Name must contain only letters and numbers, no spaces or special characters.', regex='^[a-zA-Z0-9]+$')])),
                ('authEmail', models.EmailField(max_length=254, unique=True)),
                ('authImg', models.ImageField(blank=True, default='images/default_personal.png', null=True, upload_to='images/%Y/%m/%d/personal/')),
                ('authWallpaper', models.ImageField(blank=True, default='images/default_wallpaper.png', null=True, upload_to='images/%Y/%m/%d/wallpaper/')),
                ('authBirthDate', models.DateField()),
                ('authBio', models.TextField(validators=[django.core.validators.RegexValidator(message='Bio cannot contain HTML tags.', regex='^[^<>]*$')])),
                ('authCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('authUpdatedAt', models.DateTimeField(auto_now=True)),
                ('authPassword', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='Name must contain only letters and numbers, no spaces or special characters.', regex='^[a-zA-Z0-9]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('artID', models.AutoField(primary_key=True, serialize=False)),
                ('artName', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Bio cannot contain HTML tags.', regex='^[^<>]*$')])),
                ('artImg', models.ImageField(blank=True, null=True, upload_to=api.model.Article.get_image_upload_path)),
                ('artContent', models.TextField(validators=[django.core.validators.RegexValidator(message='Bio cannot contain HTML tags.', regex='^[^<>]*$')])),
                ('artCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('artUpdatedAt', models.DateTimeField(auto_now_add=True)),
                ('artAgree', models.IntegerField(default=0)),
                ('artDisagree', models.IntegerField(default=0)),
                ('authID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='api.author')),
                ('artTags', models.ManyToManyField(blank=True, related_name='articletag', to='api.tag')),
            ],
        ),
    ]
