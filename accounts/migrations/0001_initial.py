# Generated by Django 3.0.2 on 2020-01-27 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_id', models.CharField(blank=True, max_length=10, null=True)),
                ('about_me', models.CharField(max_length=140, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=10, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('body', models.CharField(max_length=1000, null=True)),
                ('no_likes', models.BigIntegerField(default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('diary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Diary')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('Post', 'Post'), ('Comment', 'Comment')], max_length=10, null=True)),
                ('item_id', models.CharField(blank=True, max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('liked_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Diary')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.CharField(blank=True, max_length=10, null=True)),
                ('body', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Post')),
                ('posted_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
