'''Convert a given date to Absolom Reconing date'''

from datetime import datetime

from arconverter.ardate import ArDate
from arconverter.constants import arDays, arMonths, arShortMonths, arDayShort


def convert(target_date: datetime) -> ArDate:
    '''Convert a given date to Absolom Reconing date'''

    # Break the year up into pieces
    year = target_date.year
    month = target_date.month
    day = target_date.day
    # Note, the weekday() function returns 0 for Monday, 6 for Sunday
    # so we need to add 1 to map it to our dictionary
    day_of_week = target_date.weekday()+1

    # Build the resulting arDate and it's properties
    result = ArDate()
    result.year = year + 2700 # yes, after 2099 this will break...
    result.monthNum = month
    result.day = day
    result.month = arMonths[month]
    result.monthShort = arShortMonths[month]
    result.weekday = arDays[day_of_week] 
    result.weekdayNum = day_of_week
    result.weekdayShort = arDayShort[day_of_week]

    return result
