from django.shortcuts import render
from .models import Listing

# Create your view methods here.
# We have taken our database data and displayed it on our website 
# (replacing the html static markup placeholders we had).


def index(request):
    listings = Listing.objects.all()
    
    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')