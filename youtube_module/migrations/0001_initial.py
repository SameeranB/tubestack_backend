# Generated by Django 3.0.7 on 2020-10-07 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='VideoData',
            fields=[
                ('video_id', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('thumbnail', models.URLField()),
                ('channel_name', models.CharField(max_length=300)),
                ('published_at', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'VideosData',
                'ordering': ['video_id', '-published_at'],
            },
        ),
        migrations.CreateModel(
            name='VideoKeywordRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_videos', to='youtube_module.Keyword')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_keywords', to='youtube_module.VideoData')),
            ],
        ),
        migrations.AddIndex(
            model_name='videodata',
            index=models.Index(fields=['video_id', 'published_at'], name='youtube_mod_video_i_e998a9_idx'),
        ),
    ]
