from django.forms import formset_factory
from saleslog.outputlogic.usercharacterprofile import UserCharacterProfile
from saleslog.forms import GuildInput

class GuildFormBuilder(UserCharacterProfile):
    """
    Build and return guild forms.

    Members:
    character       models.Character object
    _characterName  String character name (please use the getter)
    _guilds         list of guild information:
                    {
                        'guild__name':name,
                        'guild__store_location__name':guildStoreLocationName,
                        'primar':is primary guild
                    }

    Constructor:

    Constructor initializes fields to existing values or None.  If a user is
    provided, there will be an attempt to query the database for an
    associated character and populate the members that way.

    If another UserCharacterProfile is provided and no user is provided,
    the members will be populated by reference to other.

    user        request.user from view.
    other       A different UserCharacterProfile
    """

    def getGuildFormSet(self):
        """
        Create and return a formset of guild information associated with the
        character.

        return      Form set of GuildInput if there are guilds associated with
                    this user/character, otherwise return None
        """
        if not self._guilds:
            GuildFormSet = formset_factory(GuildInput, max_num=5, absolute_max=5,can_delete=True)
            return GuildFormSet()
        
        GUILD_NAME = UserCharacterProfile.GUILD_NAME
        STORE_LOC = UserCharacterProfile.STORE_LOCATION
        IS_PRIMARY = UserCharacterProfile.IS_PRIMARY
        GuildFormSet = formset_factory(GuildInput, max_num=5, absolute_max=5,can_delete=True)
        setInitials = []
        for entry in self._guilds:
            formInitial = {
                GuildInput.GUILD_NAME : entry[GUILD_NAME],
                GuildInput.LOCATION_NAME : entry[STORE_LOC],
                GuildInput.IS_PRIMARY : entry[IS_PRIMARY],
            }
            setInitials.append(formInitial)
            
        return GuildFormSet(initial=setInitials)

    def getBlankGuildFormSet():
        """
        Class method to get a blank guild input formset
        """
        return formset_factory(GuildInput, max_num=5, absolute_max=5,can_delete=True)