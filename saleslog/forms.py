from django import forms

class AddListing(forms.Form):
    """
    Form for creating entries.
    """
    item = forms.CharField()
    quantity = forms.IntegerField(min_value=1)
    total_price = forms.IntegerField(min_value=1)
    end_date = forms.DateField()
    guild = forms.CharField(required=False)
    location = forms.CharField(required=False)
    character = forms.CharField(required=False)

class EditCharacterName(forms.Form):
    """
    Form for editing character name.
    """
    CHARACTER_NAME = 'character_name'
    character_name = forms.CharField()

class GuildInput(forms.Form):
    """
    Form for editing or adding guilds
    """
    guild = forms.CharField()
    store_location = forms.CharField(required=False)
