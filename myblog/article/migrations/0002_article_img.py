# Generated by Django 2.0.7 on 2018-09-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='articleimg'),
        ),
    ]
