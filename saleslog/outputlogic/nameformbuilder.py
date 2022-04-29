from saleslog.forms import EditCharacterName
from saleslog.outputlogic.usercharacterprofile import UserCharacterProfile


class NameFormBuilder(UserCharacterProfile):
    """
    Build a character name form.

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

    def getCharacterNameForm(self):
        """
        Create and return a form for editing this character name.

        return      EditCharacterName form object
        """
        if self._characterName:
            f = EditCharacterName(initial={
                        EditCharacterName.CHARACTER_NAME : self.characterName,
                    })
        else:
            f = EditCharacterName()
        return f