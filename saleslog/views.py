from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from saleslog import forms
from saleslog.inputlogic.profileinput import ProfileInput
from saleslog.models import Character
from saleslog.util import usercharacter
from saleslog.util import time

CHARACTER_NAME = 'character_name'
# Create your views here.
def index(request):
    context = {}
    context[CHARACTER_NAME] = usercharacter.getAssociatedCharacterName(request.user)
    return render(request, 'saleslog/index.html', context=context)

def view_listings(request):
    context = {}
    context[CHARACTER_NAME] = usercharacter.getAssociatedCharacterName(request.user)
    return render(request, 'saleslog/view_listings.html', context=context)

@login_required
def add_listing(request):
    context={}
    context[CHARACTER_NAME] = usercharacter.getAssociatedCharacterName(request.user)
    f = forms.AddListing(initial={
                                    'quantity' : 1,
                                    'total_price' : 1,
                                    'end_date' : time.todayPlus30()
                                })
    context['form'] = f
    return render(request, 'saleslog/add_listing.html', context=context)

def edit_profile(request):
    context = {}
    username = request.user.username
    context['username'] = username
    f = forms.EditProfile(initial={
                            'character_name' : 'A name',
                            'guild' : 'A guild',
                            'store_location' : 'A location',
                        })
    context['form'] = f
    return render(request, 'saleslog/edit_profile.html', context=context)

def edit_profile_submit(request):
    user = request.user
    f = forms.EditProfile(request.POST)
    if f.is_valid():
        data = f.cleaned_data
        dataIn = ProfileInput(data)
        dataIn.insertRecords(user)
        return HttpResponseRedirect(reverse('saleslog:edit_profile'))