from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from saleslog import forms
from saleslog.inputlogic.characternameinput import CharacterNameInput
from saleslog.inputlogic.characterguildinput import CharacterGuildInput
from saleslog.util import time
from saleslog.outputlogic.usercharacterprofile import UserCharacterProfile


CHARACTER_NAME = 'character_name'
# Create your views here.
def index(request):
    context = {}

    charInfo = UserCharacterProfile(request.user)
    context[CHARACTER_NAME] = charInfo.characterName
    return render(request, 'saleslog/index.html', context=context)

def view_listings(request):
    context = {}
    charInfo = UserCharacterProfile(request.user)
    context[CHARACTER_NAME] = charInfo.characterName

    return render(request, 'saleslog/view_listings.html', context=context)

@login_required
def add_listing(request):
    context={}
    charInfo = UserCharacterProfile(request.user)
    context[CHARACTER_NAME] = charInfo.characterName

    f = forms.AddListing(initial={
                                    'quantity' : 1,
                                    'total_price' : 1,
                                    'end_date' : time.todayPlus30()
                                })
    context['form'] = f
    return render(request, 'saleslog/add_listing.html', context=context)

@login_required
def edit_profile(request):
    """
    Edit profile form page.
    """
    context = {}
    # Get character info
    username = request.user.username
    context['username'] = username
    charInfo = UserCharacterProfile(request.user)

    # If character exists, get form with initial info.
    cNameForm = charInfo.getCharacterNameForm()
        
    context['f_character_name'] = cNameForm
    # build guild form.
    context['f_guilds'] = charInfo.getGuildFormSet()
    return render(request, 'saleslog/edit_profile.html', context=context)

@login_required
def edit_character_name_submit(request):
    """
    Submit changes to character name associated with request.user
    """
    user = request.user
    characterNameInput = CharacterNameInput(user, request.POST, forms.EditCharacterName)
    
    if characterNameInput.insertCharacterName():
        #Success
        print('Success')
    else:
        print('Failure')
    

    return HttpResponseRedirect(reverse('saleslog:edit_profile'))

@login_required
def edit_guilds_submit(request):
    """
    Submit changes to the guild
    """
    user = request.user
    characterGuildInput = CharacterGuildInput(user, request.POST, UserCharacterProfile.getBlankGuildFormSet())
    characterGuildInput.inputCharacterGuilds()
    return HttpResponseRedirect(reverse('saleslog:edit_profile'))