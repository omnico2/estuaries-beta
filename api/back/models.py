from django.db import models

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    banner = models.FileField()
    logo = models.FileField()
    favicon = models.FileField()
    bannertext = models.CharField(max_length=100)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40)
    img = models.FileField()
    description = models.TextField(blank=True, null=True)

def get_absolute_url(self):
    return reverse('categories', kwargs={'slug': self.slug})