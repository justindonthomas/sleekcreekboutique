from saleslog.models import Character, Guild, Location

class UserCharacter(object):
    """
    Get character name, and a structure containing guild name and loction for 
    all guilds associated with the character.
    """
    GUILD_NAME = 'guild_name'
    def __init__(self):
        self.characterName = None
        self.guilds = None

    def initialize(self, user):
        """
        Initialize character info fields.

        return false if character cannot be found.
        """
        try:
            character = Character.objects.get(user=user)
            self.characterName = character.name
            self.guilds = character.guild.all().values('name',
                                                        'store_location__name')
            print(self.guilds)
        except Character.DoesNotExist:
            return False

        return True
