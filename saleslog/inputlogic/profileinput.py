from django.core.exceptions import ValidationError
from saleslog.models import Character
from saleslog.forms import EditCharacterName

class ProfileInput(object):

    def __init__(self, data):
        """
        Initialize profile input object with cleaned data.
        """
        self.character_name = data[EditCharacterName.CHARACTER_NAME]

    def insertCharacterName(self, user):
        """
        Insert records for auth_user object user.
        """
        if user.is_anonymous:
            return False
        character, _ = Character.objects.get_or_create(user=user)
        character.name = self.character_name
        character.save()