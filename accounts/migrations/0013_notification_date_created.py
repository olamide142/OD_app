# Generated by Django 3.0.2 on 2020-02-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200204_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
