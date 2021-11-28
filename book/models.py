from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Books(models.Model):
    judul = models.CharField(max_length=50)
    slug = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super(Books, self).save(*args, **kwargs)
