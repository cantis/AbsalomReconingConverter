from datetime import datetime

from arconverter.arDate import arDate
from arconverter.constants import arDays, arMonths, arShortMonths, arDayShort


def convert(targetDate: datetime) -> arDate:
    '''Convert a given date to Absolom Reconing date'''

    # Break the year up into pieces
    year = targetDate.year
    month = targetDate.month
    day = targetDate.day
    # Note, the weekday() function returns 0 for Monday, 6 for Sunday so we need to add 1 to map it to our dictionary
    dayOfWeek = targetDate.weekday()+1

    # Build the resulting arDate and it's properties
    result = arDate()
    result.year = year + 2700 # yes, after 2099 this will break...
    result.monthNum = month
    result.day = day
    result.month = arMonths[month]
    result.monthShort = arShortMonths[month]
    result.weekday = arDays[dayOfWeek] 
    result.weekdayNum = dayOfWeek
    result.weekdayShort = arDayShort[dayOfWeek]

    return result


