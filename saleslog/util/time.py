import datetime
from datetime import timedelta

def today():
    """
    Get datetime object for today.
    """
    return datetime.date.today()

def todayPlus30():
    """
    Get current date + 30 days.
    """
    td = timedelta(days=30)
    return datetime.date.today() + td