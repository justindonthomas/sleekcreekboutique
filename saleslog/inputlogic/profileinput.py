from django.core.exceptions import ValidationError
from saleslog.forms import EditProfile
from saleslog.models import Character, Guild

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
        guild, _ = Guild.objects.get_or_create(name=self.guild)
        if user.is_anonymous:
            return False
        try:
            character = Character.objects.get(user=user)
            character.name = self.character_name
            character.save()
        except Character.DoesNotExist:
            character = Character(name=self.character_name, user=user)
        try:
            character.full_clean()
        except ValidationError as e:
            return False
        character.save()
        character.guild.add(guild)
        character.save()

        
