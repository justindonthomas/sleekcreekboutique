from django.core.exceptions import ValidationError
from saleslog.inputlogic.formprocessor import FormProcessor
from saleslog.models import Character
from saleslog.forms import EditCharacterName

class CharacterNameInput(FormProcessor):
    """
    Receive a request.post for a character name change or creation input

    super constructor args:
    
    user            request.user
    postObject      request.post
    FormType        Class of form to process.
    """
    
    def insertCharacterName(self):
        """
        Insert records for auth_user object user.
        """
        if self.cleanedData:
            character, _ = Character.objects.get_or_create(user=self.user)
            character.name = self.cleanedData[EditCharacterName.CHARACTER_NAME]
            character.save()
            return True
        else:
            return False