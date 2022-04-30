from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from saleslog import forms
from saleslog.inputlogic.characternameinput import CharacterNameInput
from saleslog.inputlogic.characterguildinput import CharacterGuildInput
from saleslog.inputlogic.listinginput import ListingInput
from saleslog.outputlogic.guildformbuilder import GuildFormBuilder
from saleslog.outputlogic.listingformbuilder import ListingFormBuilder
from saleslog.outputlogic.nameformbuilder import NameFormBuilder
from saleslog.util import time
from saleslog.outputlogic.usercharacterprofile import UserCharacterProfile


CHARACTER_NAME = 'character_name'
# Create your views here.
def index(request):
    context = {}
    charInfo = UserCharacterProfile(user=request.user)
    context[CHARACTER_NAME] = charInfo.characterName
    return render(request, 'saleslog/index.html', context=context)

def view_listings(request):
    context = {}
    charInfo = UserCharacterProfile(user=request.user)
    context[CHARACTER_NAME] = charInfo.characterName

    return render(request, 'saleslog/view_listings.html', context=context)

@login_required
def add_listing(request):
    context={}
    charInfo = ListingFormBuilder(user=request.user)
    context[CHARACTER_NAME] = charInfo.characterName

    context['form'] = charInfo.getAddListingForm()
    return render(request, 'saleslog/add_listing.html', context=context)

@login_required
def add_listing_submit(request):
    listingProcessor = ListingInput(request.user, request.POST, forms.AddListing)
    listingProcessor.insertListing()
    return HttpResponseRedirect(reverse('saleslog:add_listing'))

@login_required
def edit_profile(request):
    """
    Edit profile form page.
    """
    context = {}
    # Get character info
    username = request.user.username
    context['username'] = username
    charInfo = NameFormBuilder(user=request.user)

    # If character exists, get form with initial info.
    cNameForm = charInfo.getCharacterNameForm()
        
    context['f_character_name'] = cNameForm
    # build guild form.
    charGuilds = GuildFormBuilder(other=charInfo)
    context['f_guilds'] = charGuilds.getGuildFormSet()
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
    characterGuildInput = CharacterGuildInput(user, request.POST, GuildFormBuilder.getBlankGuildFormSet())
    characterGuildInput.inputCharacterGuilds()
    return HttpResponseRedirect(reverse('saleslog:edit_profile'))