from saleslog.forms import EditProfile
from saleslog.models import Character, Guild, Location, UserCharacter

class ProfileInput(object):

    def __init__(self, data):
        """
        Initialize profile input object with cleaned data.
        """
        self.character_name = data[EditProfile.CHARACTER_NAME]
        self.guild = data[EditProfile.GUILD]
        self.store_location = data[EditProfile.STORE_LOCATION]

    def insertRecords(self, user):
        """
        Insert records for auth_user object user.
        """
        storeLoc, _ = Location.objects.get_or_create(name=self.store_location)
        guild, _ = Guild.objects.get_or_create(name=self.guild,
                                            store_location=storeLoc)
        character, _ =  Character.objects.get_or_create(name=self.character_name, user=user)
        character.guild.add(guild)
        character.save()

        
