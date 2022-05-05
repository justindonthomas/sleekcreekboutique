from django.core.exceptions import MultipleObjectsReturned
from django.db  import IntegrityError
from saleslog.forms import GuildInput
from saleslog.inputlogic.formprocessor import FormProcessor
from saleslog.models import Character, CharacterGuild, Guild, Location

class CharacterGuildInput(FormProcessor):
    """
    Receive a request.post for a character guilds change or creation input.

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

    def inputCharacterGuilds(self):
        """
        Edit or create character guild entries.
        """
        # Data: {'entry_id': 16, 'guild': 'The Best Guild', 'store_location': 'Rawlka', 'is_primary': True, 'DELETE': False}
        try:
            character = Character.objects.get(user=self.user)
        except (Character.DoesNotExist, MultipleObjectsReturned) as e:
            print(e)
            return False
        if self.cleanedData:
            for item in self.cleanedData:
                if item:
                    if item['DELETE'] and item[GuildInput.GUILD_ID]:
                        try:
                            guild = Guild.objects.get(id=item[GuildInput.GUILD_ID])
                        except (Guild.DoesNotExist, MultipleObjectsReturned) as e:
                            print(e)
                            return False
                        try:
                            charGuild = CharacterGuild.objects.get(character=character,
                                                                    guild=guild)
                            charGuild.delete()
                        except (CharacterGuild.DoesNotExist, MultipleObjectsReturned) as e:
                            print(e)
                            return False
                    else:
                        if item[GuildInput.GUILD_ID]:
                            guild = Guild.objects.get(id=item[GuildInput.GUILD_ID])
                        else:
                            guild,_ = Guild.objects.get_or_create(name=item[GuildInput.GUILD_NAME])
                        if item[GuildInput.LOCATION_NAME] and not item[GuildInput.LOCATION_NAME].isspace():
                            location,_ = Location.objects.get_or_create(name=item[GuildInput.LOCATION_NAME])
                            guild.store_location = location

                        guild.name=item[GuildInput.GUILD_NAME]
                        guild.save()
                        charGuild,_ = CharacterGuild.objects.get_or_create(guild=guild,
                                                                character=character)
                        charGuild.primary = item[GuildInput.IS_PRIMARY]
                        try:
                            charGuild.full_clean()
                            charGuild.save()
                        except IntegrityError as e:
                            print(e)
                            return False
            return True
        else:
            return False
