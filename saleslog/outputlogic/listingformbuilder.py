from saleslog.models import Character


class ListingFormBuilder(object):
    def __init__(self, userCharacterProfile):
        self._characterName = None
        try:
            character = Character.objects.get(user=self.user)
        except (Character.DoesNotExist, Character.MultipleObjectsReturned) as e:
            print(e)
            character = None