from django.core.exceptions import MultipleObjectsReturned
from django.db  import IntegrityError
from django.forms import ValidationError
from saleslog.inputlogic.formprocessor import FormProcessor
from saleslog.forms import GuildInput
from saleslog.models import Character, CharacterGuild, Guild, Location

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

    def deleteCharacterGuildRecord(self, cname, gname):
        """
        Try to remove a character guild association from the database.

        cname       Character name.
        gname       Guild name.
        """

    def inputCharacterGuilds(self):
        """
        Edit or create character guild entries.
        """
        # Data: {'guild': 'a', 'store_location': 'b', 'is_primary': False, 'DELETE': False}
        try:
            character = Character.objects.get(user=self.user)
        except (Character.DoesNotExist, MultipleObjectsReturned) as e:
            print(e)
            return False

        if self.cleanedData:
            for item in self.cleanedData:
                if item['DELETE']:
                    try:
                        guild = Guild.objects.get(name__iexact=item['guild'])
                    except (Guild.DoesNotExist, MultipleObjectsReturned) as e:
                        print(e)
                        return False
                    try:
                        charGuild = CharacterGuild.objects.get(character=character,
                                                                guild=guild)
                        charGuild.delete()
                    except (Guild.DoesNotExist, MultipleObjectsReturned) as e:
                        print(e)
                        return False
                else:
                    location,_ = Location.objects.get_or_create(name=item['store_location'])
                    guild,_ = Guild.objects.get_or_create(name=item['guild'])
                    guild.store_location = location
                    guild.save()
                    charGuild,_ = CharacterGuild.objects.get_or_create(guild=guild,
                                                            character=character)
                    try:
                        charGuild.full_clean()
                        charGuild.save()
                    except IntegrityError as e:
                        print(e)
                        return False
                    
            # character, _ = Character.objects.get_or_create(user=self.user)
            # character.name = self.cleanedData[EditCharacterName.CHARACTER_NAME]
            # character.save()
            return True
        else:
            return False
