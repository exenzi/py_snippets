from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from transliterate import slugify as translit_slugify
from django.utils.text import slugify

User = get_user_model()

# Create your models here.
class Snippet(models.Model):
    title = models.CharField("Название", max_length=100, db_index=True)
    slug = models.SlugField(max_length=100)
    code = models.TextField("Код", db_index=True)
    description = models.TextField("Описание")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    view_count = models.IntegerField("Кол-во просмотров", default=0)
    tags = models.ManyToManyField('Tag', verbose_name="Тэг", blank=True, related_name='snippets')

    def get_absolute_url(self):
        return reverse('snippet', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = translit_slugify(self.title) or slugify(self.title)
        super().save(*args, **kwargs)
        self.slug = f"{self.id}-{slug}"
        return super().save(*args, **kwargs)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = translit_slugify(self.title) or slugify(self.title)            
        return super().save(*args, **kwargs)
