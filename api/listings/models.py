from django.db import models
from django.conf import settings
from back.models import Categories
from users.models import CustomUser
from django_userforeignkey.models.fields import UserForeignKey
from autoslug import AutoSlugField
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Listing(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[alphanumeric])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField()
    description = models.TextField(blank=True, null=True)
    #categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    #author = models.ForeignKey(CustomUser, to_field='username', default=None, on_delete=models.CASCADE)
    author_id = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', unique=True, validators=[alphanumeric])

    def __str__(self):
        return self.name

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.listing.name