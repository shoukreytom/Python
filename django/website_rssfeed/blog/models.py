from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = [('published', 'Published'), ('draft', 'Draft')]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='draft')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


@receiver(post_save, sender=Post)
def save_slug(sender, instance=None, created=False, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()
