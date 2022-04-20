from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

class AbstractThing(models.Model):
  name = models.CharField(max_length=255)

  class Meta:
    abstract = True

class Character(AbstractThing):
  """
  Name of a character.
  """
  pass

class Guild(AbstractThing):
  """
  Name of a guild.
  """
  pass

class Item(AbstractThing):
  """
  Name of an item.
  """
  pass

class Location(AbstractThing):
  """
  Name of a location.
  """
  pass

class Listing(models.Model):
  """
  Guild store listing entry.

  item        Item for sale.
  quantity    Number of items for sale.
  total_price Total sell price of listing.
  end_date    Estimated end time of listing.
  guild       Name of the selling guildstore.
  location    Name of the location of the guild trader.
  character   Name of the character selling the item.
  """
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
  total_price = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])
  end_date = models.DateTimeField()
  guild = models.ForeignKey(Guild, on_delete=models.DO_NOTHING, blank=True, null=True)
  location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
  character = models.ForeignKey(Character, on_delete=models.DO_NOTHING, blank=True, null=True)

class Sale(models.Model):
  """
  Sale of a listing.

  listing     Listing that was sold.
  net_price   Amount received by player for sale (Listing total_price minus
              fees).
  """
  listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
  net_price = models.PositiveIntegerField(validators=[MinValueValidator(1)])

class UserCharacter(models.Model):
  """
  Map of users to characters.

  user      auth User object.
  character Associated character.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  character = models.ForeignKey(Character, on_delete=models.CASCADE)




