from django.shortcuts import render

# Create your views methods here. The methods you use in urls are made here.


def index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
