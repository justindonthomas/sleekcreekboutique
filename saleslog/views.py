from django.shortcuts import render

# Create your views here.
def index(request):
  context = {}
  return render(request, 'saleslog/index.html', context=context)

def view_listings(request):
  context = {}
  return render(request, 'saleslog/view_listings.html', context=context)

def add_listing(request):
  context={}
  return render(request, 'saleslog/add_listing.html', context=context)