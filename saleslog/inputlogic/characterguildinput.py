from saleslog.inputlogic.formprocessor import FormProcessor
from saleslog.forms import GuildInput

class CharacterGuildInput(FormProcessor):
    """
    Receive a request.post for a character guilds change or creation input.

    super constructor args:
    
    user            request.user
    postObject      request.post
    FormType        Class of form to process.
    """

    def inputCharacterGuilds(self):
        """
        Edit or create character guild entries.
        """
