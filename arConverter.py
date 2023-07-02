import datetime
from arConverter import convert
from arDate import arDate
from constants import arDays, arMonths, arShortMonths

def convert(targetDate: datetime.datetime) -> arDate:
    '''Convert target date to AR date'''



if __name__ == "__main__":
    targetDate = datetime.datetime(2023, 1, 1)
    arDate = convert(targetDate)




