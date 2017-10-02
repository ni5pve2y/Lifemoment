from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    context = models.CharField(max_length=10000)
    image = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    edited = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        super().save()


class Comment(models.Model):
    user = models.ForeignKey(User)
    context = models.CharField(max_length=10000)
    post = models.ForeignKey(Post)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    edited = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.context
