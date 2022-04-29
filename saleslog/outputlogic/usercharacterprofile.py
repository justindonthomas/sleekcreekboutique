from django.forms import formset_factory

from saleslog.forms import EditCharacterName, GuildInput
from saleslog.models import Character, CharacterGuild


class UserCharacterProfile(object):
    """
    Get character name, and a structure containing guild name and loction name
    for all guilds associated with the character.
    """
    GUILD_NAME = 'guild__name'
    STORE_LOCATION = 'guild__store_location__name'
    IS_PRIMARY = 'primary'

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
                                                    'guild__store_location__name',
                                                    'primary')
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



        
