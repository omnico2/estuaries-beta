from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ['name']
    # ordering = ['-created_at']


admin.site.register(Listing, ListingAdmin)
