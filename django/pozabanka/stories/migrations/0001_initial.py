# Generated by Django 3.2.9 on 2022-01-24 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('articles', models.ManyToManyField(related_name='story_articles', to='articles.Article')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='story_author', to=settings.AUTH_USER_MODEL)),
                ('dislikes', models.ManyToManyField(related_name='story_dislike', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='story_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
