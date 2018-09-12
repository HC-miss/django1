# Generated by Django 2.0.7 on 2018-09-04 11:33

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', tinymce.models.HTMLField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('read_num', models.PositiveIntegerField(default=0)),
                ('collect_num', models.PositiveIntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='uname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User'),
        ),
    ]