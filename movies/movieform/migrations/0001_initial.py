# Generated by Django 3.1.7 on 2021-03-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMusicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=50, verbose_name='Movie Name')),
                ('m_year', models.CharField(max_length=10, verbose_name='Movie Year')),
                ('m_actors', models.CharField(max_length=100, verbose_name='Movie Actors')),
                ('m_rank', models.CharField(max_length=3, verbose_name='Movie Rank Point')),
                ('m_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Movie Image')),
            ],
        ),
    ]
