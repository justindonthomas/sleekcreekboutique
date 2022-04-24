from saleslog.forms import EditCharacterName
from saleslog.models import Character, CharacterGuild, Guild, Location


class UserCharacterProfile(object):
    """
    Get character name, and a structure containing guild name and loction for 
    all guilds associated with the character.
    """
    GUILD_NAME = 'name'
    STORE_NAME = 'store_location__name'

    def __init__(self, user):
        """
        Constructor initializes fields to existing values or None
        Generates a new Character record if it does not exist.

        user        request.user from view.
        """
        try:
            character = Character.objects.get(user=user)
            self._characterName = character.name
            self._guilds = CharacterGuild.objects.filter(character=character)   \
                                            .select_related('store_location')  \
                                            .values('guild__name',
                                                    'guild__store_location__name')
            print(self._guilds)
        except (Character.DoesNotExist, TypeError):
            self._characterName = None
            self._guilds = None

    @property
    def characterName(self):
        """
        Getter for _characterName.

        If the name exists, return the name, otherwise return the string "None"
        """
        if self._characterName:
            return self._characterName
        else:
            return "None"
    
    @property
    def guilds(self):
        """
        Return the _guilds dictionary.
        """
        return self._guilds

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
