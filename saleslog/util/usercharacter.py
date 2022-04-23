from saleslog.models import Character, Guild, Location

class UserCharacter(object):
    def __init__(self):
        self.characterName = None
        self.guildNames = None
        self.guildLocations = None

    def initialize(self, user):
        """
        Initialize character info fields.

        return false if character cannot be found.
        """
        try:
            character = Character.objects.get(user=user)
 
        except:
            return False

        self.characterName = character.name

        return True