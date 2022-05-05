from django import forms

class AddListing(forms.Form):
    """
    Form for creating entries.
    """
    # Field strings for setting initial values
    ITEM = "item"
    QTY = "quantity"
    TOTAL_PRICE = "total_price"
    END_DATE = "end_date"
    GUILD_NAME = "guild"
    LOC = "location"
    CHARACTER = "character"

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
    # Field string for setting initial values
    CHARACTER_NAME = 'character_name'

    character_name = forms.CharField()

class GuildInput(forms.Form):
    """
    Form for editing or adding guilds
    """
    # Field strings for setting initial values
    GUILD_ID = 'entry_id'
    GUILD_NAME = 'guild'
    LOCATION_NAME = 'store_location'
    IS_PRIMARY = 'is_primary'
    entry_id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    guild = forms.CharField()
    store_location = forms.CharField(required=False)
    is_primary = forms.BooleanField(required=False)
