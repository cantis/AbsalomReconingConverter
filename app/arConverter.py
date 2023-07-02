from datetime import date, datetime
from arDate import arDate
from constants import arDays, arMonths, arShortMonths


def convert(targetDate: datetime) -> arDate:
    '''Convert target date to AR date'''
    # get the year
    year = targetDate.year
    month = targetDate.month
    day = targetDate.day
    dayOfWeek = targetDate.weekday()+1

    result = arDate()
    result.year = year + 2700 # yes, after 2099 this will break...
    result.monthNum = month
    result.day = day
    result.month = arMonths[month]
    result.monthShort = arShortMonths[month]
    result.weekday = arDays[dayOfWeek]
    result.weekdayNum = dayOfWeek

    return result

if __name__ == "__main__":
    targetDate = date.today()
    arDate = convert(targetDate)
    print(arDate.weekdayDate())
