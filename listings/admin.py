from django.contrib import admin
from .models import Listing
# Register your models here. We can customise our admin stuff for the listings app.

# The code below is to make edits to to listings page in the admin area - to add more data (price, list date, etc).

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    # This is to check and un-check the published button
    list_editable = ('is_published',) 
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # This is to add pagination (page 1, 2, etc to break up pages)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
