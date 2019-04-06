from django.db import models
from django.urls import reverse


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url_edit(self):
            return reverse('dog_app:edit', kwargs={'dog_id': self.id})

    def get_absolute_url_update(self):
            return reverse('dog_app:update', kwargs={'dog_id': self.id})

    def get_absolute_url_delete(self):
            return reverse('dog_app:delete', kwargs={'dog_id': self.id})

    class Meta:
        ordering = '-updated_at',
        verbose_name = 'dog'
        verbose_name_plural = 'dogs'
