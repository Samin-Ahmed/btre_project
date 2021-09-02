from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # this is the homepage, that's why we left it blank.
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]

# This is a routing file - we put in paths inside that "urlpatterns" list.
# The path will have a "/" at the end is usually linked to a "view method" or link to a URL from another file.
# In this example, we are linking to the admin URLS (first url at current time - 2/9/21).
# Every app we create (like listing, about us, etc) it will create a new folder, let's say "Listings", and
# we'll create a new "url.py" in that listings app and then bring that into this main "url.py".
# This is the collection of all of our apps URLs.
