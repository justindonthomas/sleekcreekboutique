from django.core.exceptions import ValidationError
from saleslog.inputlogic.formprocessor import FormProcessor
from saleslog.models import Character
from saleslog.forms import EditCharacterName

class CharacterNameInput(FormProcessor):
    """
    Receive a request.post for a character name change or creation input

    Members:

    user            request.user
    cleanedData     Cleaned data from form.
    """
    def __init__(self, user, postObject, FormType):
        """
        Receive a request.post and store cleaned data.

        Constructor args:

        user            request.user
        postObject      request.post
        FormType        Class of form to process.

        Members:

        user            request.user
        cleanedData     Cleaned data from form.
        """
        super().__init__(user, postObject, FormType)

    def insertCharacterName(self):
        """
        Insert records for auth_user object user.

        return      True on success
        """
        if self.cleanedData:
            character, _ = Character.objects.get_or_create(user=self.user)
            character.name = self.cleanedData[EditCharacterName.CHARACTER_NAME]
            character.save()
            return True
        else:
            return False