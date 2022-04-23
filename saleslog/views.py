from django.shortcuts import render

from saleslog import forms
from saleslog.util import time

# Create your views here.
def index(request):
    context = {}
    return render(request, 'saleslog/index.html', context=context)

def view_listings(request):
    context = {}
    return render(request, 'saleslog/view_listings.html', context=context)

def add_listing(request):
    context={}
    f = forms.AddListing(initial={
                                    'quantity' : 1,
                                    'total_price' : 1,
                                    'end_date' : time.todayPlus30()
                                })
    context['form'] = f
    return render(request, 'saleslog/add_listing.html', context=context)

def edit_profile(request):
    context = {}
    f = forms.EditProfile()
    context['form'] = f
    return render(request, 'saleslog/edit_profile.html', context=context)