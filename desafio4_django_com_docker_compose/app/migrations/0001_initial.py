# Generated by Django 3.0.6 on 2020-07-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.TextField(verbose_name='image url')),
                ('video_url', models.TextField(blank=True, default=None, null=True, verbose_name='video url')),
                ('live_date', models.DateTimeField(verbose_name='live date')),
            ],
        ),
    ]
