from saleslog.inputlogic.formprocessor import FormProcessor
from saleslog.forms import GuildInput
from saleslog.models import Guild, Location

class CharacterGuildInput(FormProcessor):
    """
    Receive a request.post for a character guilds change or creation input.

    super constructor args:
    
    user            request.user
    postObject      request.post
    FormType        Class of form to process.

    Members:

    user            request.user
    cleanedData     Cleaned data from form.
    """

    def inputCharacterGuilds(self):
        """
        Edit or create character guild entries.
        """
        if self.cleanedData:
            for item in self.cleanedData:
                print("Data:", item)
            # character, _ = Character.objects.get_or_create(user=self.user)
            # character.name = self.cleanedData[EditCharacterName.CHARACTER_NAME]
            # character.save()
            return True
        else:
            return False
