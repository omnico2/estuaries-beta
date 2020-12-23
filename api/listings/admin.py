from django.contrib import admin
from .models import Listing, ListingImage

 
class ListingImageAdmin(admin.StackedInline):
    model = ListingImage
 
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageAdmin]
 
    class Meta:
       model = Listing
 
@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    pass

