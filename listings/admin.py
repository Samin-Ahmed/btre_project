from django.contrib import admin
from .models import Listing
# Register your models here. We can customise our admin stuff for the listings app.

admin.site.register(Listing)
