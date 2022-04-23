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

class EditProfile(forms.Form):
    """
    Form for editing character profile.
    """
    character_name = forms.CharField()
    guild = forms.CharField(required=False)
    store_location = forms.CharField(required=False)