import uuid
from django.db import models
from pozabanka.lib.utils import get_unique_slug_with_uuid
from pozabanka.users.models import User


class Article(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    slug = models.SlugField(null=False, unique=True, blank=False)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=600, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="article_author",
    )
    event_date = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="article_likes")
    dislikes = models.ManyToManyField(User, related_name="article_dislikes")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug_with_uuid(self.title)
        return super().save(*args, **kwargs)


class Source(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    cover_url = models.URLField(max_length=255, null=False, blank=False)
    title = models.CharField(
        max_length=255, blank=False
    )  # get automaticaly in the future?
    article = models.ForeignKey(
        Article, on_delete=models.SET_NULL, null=True, blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="source_author",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
