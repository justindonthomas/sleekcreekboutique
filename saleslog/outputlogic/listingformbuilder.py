from ast import Add
from saleslog.forms import AddListing
from saleslog.models import Character
from saleslog.outputlogic.usercharacterprofile import UserCharacterProfile
from saleslog.util import time

class ListingFormBuilder(UserCharacterProfile):
    """
    Build and return listing forms.

    Members:
    character       models.Character object
    _characterName  String character name (please use the getter)
    _guilds         list of guild information: (please use the getter)
                    {
                        'guild__name':name,
                        'guild__store_location__name':guildStoreLocationName,
                        'primary':is primary guild
                    }
    """
    def __init__(self, user=None, other=None):
        """
        Constructor initializes fields to existing values or None.  If a user is
        provided, there will be an attempt to query the database for an
        associated character and populate the members that way.

        If another UserCharacterProfile is provided and no user is provided,
        the members will be populated by reference to other.

        user        request.user from view.
        other       A different UseerCharacterProfile
        """
        super().__init__(user, other)
    
    def getAddListingForm(self):
        """
        Get an add listing form for a character with initials based on the
        UserCharacterProfile.
        """
        initialValues = {
                            'quantity' : 1,
                            'total_price' : 1,
                            'end_date' : time.todayPlus30()
                        }

        for guild in self.guilds:
            if guild[UserCharacterProfile.IS_PRIMARY]:
                if guild[UserCharacterProfile.GUILD_NAME]:
                    initialValues[AddListing.GUILD_NAME] = guild[UserCharacterProfile.GUILD_NAME]
                if guild[UserCharacterProfile.STORE_LOCATION]:
                    initialValues[AddListing.LOC] = guild[UserCharacterProfile.STORE_LOCATION]
        if self._characterName:
            initialValues[AddListing.CHARACTER] = self.characterName

        return AddListing(initial=initialValues)
        
