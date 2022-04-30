from django.db import IntegrityError
from saleslog.forms import AddListing
from saleslog.inputlogic.formprocessor import FormProcessor
from saleslog.models import Character, Guild, Item, Listing, Location


class ListingInput(FormProcessor):
    """
    Input a new listing.

    Members:

    user            request.user
    cleanedData     Cleaned data from form
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

    def insertListing(self):
        """
        Insert a new listing with the data in cleanedData

        {'item': 'stuff',
        'quantity': 1,
        'total_price': 1,
        'end_date': datetime.date(2022, 5, 30),
        'guild': 'c',
        'location': 'd',
        'character': 'A'}
        """
        itemName = self.cleanedData.get(AddListing.ITEM)
        qty = self.cleanedData.get(AddListing.QTY)
        price = self.cleanedData.get(AddListing.TOTAL_PRICE)
        endDate = self.cleanedData.get(AddListing.END_DATE)
        guildName = self.cleanedData.get(AddListing.GUILD_NAME)
        location = self.cleanedData.get(AddListing.LOC)
        characterName = self.cleanedData.get(AddListing.CHARACTER)

        itemObj, _ = Item.objects.get_or_create(name=itemName)
        guildObj, _ = Guild.objects.get_or_create(name=guildName)
        locationObj, _ = Location.objects.get_or_create(name=location)
        characterObj, _ = Character.objects.get_or_create(name=characterName)

        if not guildObj.store_location:
            guildObj.store_location = locationObj
            try:
                guildObj.full_clean()
                guildObj.save()
            except IntegrityError as e:
                print(e)
                return False

        newListing = Listing(item=itemObj,
                            quantity=qty,
                            total_price=price,
                            end_date=endDate,
                            guild=guildObj,
                            location=guildObj.store_location,
                            character=characterObj,
                            posted_by=self.user)
        
        try:
            newListing.full_clean()
            newListing.save()
        except IntegrityError as e:
            print(e)
            return False
        return True