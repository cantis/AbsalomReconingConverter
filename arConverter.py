import datetime
from arDate import arDate
from constants import arDays, arMonths, arShortMonths

def convert(targetDate: datetime.datetime) -> arDate:
    '''Convert target date to AR date'''
    raise NotImplementedError


if __name__ == "__main__":
    targetDate = datetime.datetime(2023, 7, 10)
    arDate = convert(targetDate)




