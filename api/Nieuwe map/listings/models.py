from django.db import models
from django.conf import settings
from back.models import Categories
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

class Listing(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField()
    description = models.TextField(blank=True, null=True)
    #categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    author_id = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=40)

#from autoslug import AutoSlugField
#slug = AutoSlugField(populate_from='username')        