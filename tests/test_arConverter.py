'''Base tests for arConverter.py'''

import datetime

from arconverter.arconverter import convert


def test_convert_base_ok():
    '''Test the base conversion'''
    # arrange
    target_date = datetime.datetime(2023, 7, 10)

    # act
    ar_date = convert(target_date)

    # assert
    assert ar_date.month == 'Erastus'
    assert ar_date.day == 10
    assert ar_date.year == 4723
    assert ar_date.weekday == 'Moonday'
    assert ar_date.weekdayNum == 1
    assert ar_date.monthNum == 7
    assert ar_date.monthShort == 'Era'


def test_short_ar_date_ok():
    '''Test the short date conversion'''
    # arrange
    target_date = datetime.datetime(2023, 7, 10)

    # act
    ar_date = convert(target_date)
    result = ar_date.short_date()

    # assert
    assert result == 'Era 10, 4723'


def test_long_ar_date_ok():
    '''Test the long date conversion'''
    # arrange
    target_date = datetime.datetime(2023, 7, 10)

    # act
    ar_date = convert(target_date)
    result = ar_date.long_date()

    # assert
    assert result == 'Erastus 10, 4723'


def test_weekday_ar_date_ok():
    '''Test the weekday date conversion'''
    # arrange
    target_date = datetime.datetime(2023, 7, 10)

    # act
    ar_date = convert(target_date)
    result = ar_date.weekday_date()

    # assert
    assert result == 'Moonday Erastus 10, 4723'


def test_normal_year_ok():
    '''Test a normal year conversion'''
    # arrange
    target_date = datetime.datetime(2023, 2, 28)

    # act
    ar_date = convert(target_date)

    # assert
    assert ar_date.day == 28
    assert ar_date.weekday == 'Toilday'


def test_leap_year_ok():
    '''Test a leap year conversion'''
    # arrange
    target_date = datetime.datetime(2024, 2, 29)

    # act
    ar_date = convert(target_date)

    # assert
    assert ar_date.day == 29
    assert ar_date.weekday == 'Oathday'