from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/
        # return reverse('blogs:detail', kwargs={'pk': self.pk})
        return reverse('blogs:index')
