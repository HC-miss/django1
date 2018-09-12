# Generated by Django 2.0.7 on 2018-09-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, unique=True)),
                ('pwd', models.CharField(max_length=20)),
                ('userinfo', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(null=True, upload_to='userimg')),
                ('email', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]