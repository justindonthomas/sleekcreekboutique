from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from saleslog.util import time


class AbstractThing(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

class Character(AbstractThing):
    """
    Name of a character.
    """
    guild = models.ManyToManyField('Guild')
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                                        blank=True,
                                                        null=True)
    

class Guild(AbstractThing):
    """
    Name and location of a guild.
    """
    store_location = models.ForeignKey('Location', blank=True, null=True,
                                                    on_delete=models.DO_NOTHING)

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
    post_date   Date listing created in database (not necessarily real posting
                date).
    end_date    Estimated end time of listing.
    guild       Name of the selling guildstore.
    location    Name of the location of the guild trader.
    character   Name of the character selling the item.
    posted_by   Auth user who created the listing.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    total_price = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])
    post_date = models.DateTimeField(default=time.today())
    end_date = models.DateTimeField(default=time.todayPlus30())
    guild = models.ForeignKey(Guild, on_delete=models.DO_NOTHING,
                                                        blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING,
                                                        blank=True, null=True)
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING,
                                                        blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                                        blank=True, null=True)

class Sale(models.Model):
    """
    Sale of a listing.

    listing     Listing that was sold.
    net_price   Amount received by player for sale (Listing total_price minus
                            fees).
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    net_price = models.PositiveIntegerField(validators=[MinValueValidator(1)])



