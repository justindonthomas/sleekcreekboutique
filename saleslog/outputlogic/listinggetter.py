from saleslog.models import Listing
from saleslog.util import time


class ListingGetter(object):
    """
    Get listings from the database.
    """
    # Objects values strings.
    ITEM = 'item__name'
    QTY = 'quantity'
    TOTAL_PRICE = 'total_price'
    END_DATE = 'end_date'
    GUILD = 'guild__name'
    LOCATION = 'location__name'
    CHARACTER = 'character__name'

    # Context key strings
    C_LISTINGS = 'listings'
    C_ITEM = 'item'
    C_QTY = 'qty'
    C_UNIT_PRICE = 'unit_price'
    C_TOTAL_PRICE = 'total_price'
    C_END_DATE = 'end_date'
    C_GUILD = 'guild'
    C_LOC = 'loc'
    C_CHARACTER = 'character'

    def getActiveListingsForCharacter(self, character):
        """
        Get listings for a character that haven't expired and return a dictionary
        for the context to build a listing table.

        character       The character to fetch the listings for.
        """
        listings = Listing.objects.filter(character=character,
                                        end_date__gte=time.today())            \
                                        .order_by('-end_date')                 \
                                        .select_related('item')                \
                                        .select_related('location')            \
                                        .select_related('guild')               \
                                        .values(ListingGetter.ITEM,
                                                ListingGetter.QTY,
                                                ListingGetter.TOTAL_PRICE,
                                                ListingGetter.END_DATE,
                                                ListingGetter.GUILD,
                                                ListingGetter.LOCATION,
                                                ListingGetter.CHARACTER)
        listingContext = []
        for listing in listings:
            unitPrice = float(listing[ListingGetter.TOTAL_PRICE]) / float(listing[ListingGetter.QTY])
            endDate = listing.get(ListingGetter.END_DATE).strftime("%d %b, %Y")
            listingContext.append({
                ListingGetter.C_ITEM : listing.get(ListingGetter.ITEM),
                ListingGetter.C_QTY : listing.get(ListingGetter.QTY),
                ListingGetter.C_UNIT_PRICE : "{:.2f}".format(unitPrice),
                ListingGetter.C_TOTAL_PRICE : listing.get(ListingGetter.TOTAL_PRICE),
                ListingGetter.C_END_DATE : endDate,
                ListingGetter.C_GUILD : listing.get(ListingGetter.GUILD),
                ListingGetter.C_LOC : listing.get(ListingGetter.LOCATION),
                ListingGetter.C_CHARACTER : listing.get(ListingGetter.CHARACTER),
            })
        return listingContext