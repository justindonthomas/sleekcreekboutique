from saleslog.models import Character

def getAssociatedCharacterName(user):
    """
    Get character name associated with the user.
    """
    try:
        character = Character.objects.get(user=user)
        return character.name
    except Character.DoesNotExist:
        return "None"