import datetime
import pytest

from arConverter import convert

def test_convert_ok():
    # arrange
    targetDate = datetime.datetime(2023, 7, 10)

    # act
    arDate = convert(targetDate)

    # assert
    assert arDate.month == "Erastus"
    assert arDate.day == 10
    assert arDate.year == 4723
    assert arDate.weekday == "Moonday"
    assert arDate.weekdayNum == 1
    assert arDate.monthNum == 7
    assert arDate.monthShort == "Era"
    assert arDate.monthLong == "Erastus"
    
