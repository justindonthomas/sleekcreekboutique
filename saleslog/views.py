from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from saleslog import forms
from saleslog.inputlogic.profileinput import ProfileInput
from saleslog.models import Character
from saleslog.util import time
from saleslog.util.usercharacter import UserCharacter


CHARACTER_NAME = 'character_name'
# Create your views here.
def index(request):
    context = {}

    charInfo = UserCharacter()
    if charInfo.initialize(request.user):
        context[CHARACTER_NAME] = charInfo.characterName
    else:
        context[CHARACTER_NAME] = "None."
    return render(request, 'saleslog/index.html', context=context)

def view_listings(request):
    context = {}
    charInfo = UserCharacter()
    if charInfo.initialize(request.user):
        context[CHARACTER_NAME] = charInfo.characterName
    else:
        context[CHARACTER_NAME] = "None."
    return render(request, 'saleslog/view_listings.html', context=context)

@login_required
def add_listing(request):
    context={}
    charInfo = UserCharacter()
    if charInfo.initialize(request.user):
        context[CHARACTER_NAME] = charInfo.characterName
    else:
        context[CHARACTER_NAME] = "None."
    f = forms.AddListing(initial={
                                    'quantity' : 1,
                                    'total_price' : 1,
                                    'end_date' : time.todayPlus30()
                                })
    context['form'] = f
    return render(request, 'saleslog/add_listing.html', context=context)

@login_required
def edit_profile(request):
    context = {}
    username = request.user.username
    context['username'] = username
    charInfo = UserCharacter()
    success = charInfo.initialize(request.user)
    if success:
        f = forms.EditProfile(initial={
                                'character_name' : charInfo.characterName,
                                'guild' : charInfo.guildNames,
                                'store_location' : charInfo.guildLocations,
                            })
    else:
        f = forms.EditProfile()
        
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