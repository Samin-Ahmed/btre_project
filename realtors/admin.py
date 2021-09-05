from django.contrib import admin
from .models import Realtor
# Register your models here.
# We are changing and addings things to the realtor page on the admin page on local host. This will increase usability. 

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)