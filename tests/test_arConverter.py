import datetime

from app.arConverter import convert


def test_convert_base_ok():
    # arrange
    targetDate = datetime.datetime(2023, 7, 10)

    # act
    arDate = convert(targetDate)

    # assert
    assert arDate.month == 'Erastus'
    assert arDate.day == 10
    assert arDate.year == 4723
    assert arDate.weekday == 'Moonday'
    assert arDate.weekdayNum == 1
    assert arDate.monthNum == 7
    assert arDate.monthShort == 'Era'


def test_short_arDate_ok():
    # arrange
    targetDate = datetime.datetime(2023, 7, 10)

    # act
    arDate = convert(targetDate)
    result = arDate.shortDate()

    # assert
    assert result == 'Era 10, 4723'


def test_long_arDate_ok():
    # arrange
    targetDate = datetime.datetime(2023, 7, 10)

    # act
    arDate = convert(targetDate)
    result = arDate.longDate()

    # assert
    assert result == 'Erastus 10, 4723'


def test_weekday_arDate_ok():
    # arrange
    targetDate = datetime.datetime(2023, 7, 10)

    # act
    arDate = convert(targetDate)
    result = arDate.weekdayDate()

    # assert
    assert result == 'Moonday Erastus 10, 4723'


def test_normal_year_ok():
    # arrange
    targetDate = datetime.datetime(2023, 2, 28)

    # act
    arDate = convert(targetDate)

    # assert
    assert arDate.day == 28
    assert arDate.weekday == 'Toilday'


def test_leap_year_ok():
    # arrange
    targetDate = datetime.datetime(2024, 2, 29)

    # act
    arDate = convert(targetDate)

    # assert
    assert arDate.day == 29
    assert arDate.weekday == 'Oathday'