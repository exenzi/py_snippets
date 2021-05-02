from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.utils.text import slugify
from transliterate import slugify as translit_slugify

User = get_user_model()

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100)
    code = models.TextField(db_index=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    view_count = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True, related_name='snippets')

    def get_absolute_url(self):
        return reverse('snippet', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = translit_slugify(self.title)
        super().save(*args, **kwargs)
        self.slug = f"{self.id}-{slug}"
        return super().save(*args, **kwargs)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
