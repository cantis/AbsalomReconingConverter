"""Convert dates to Absolom Reconing calendar system.

Examples:
    >>> from datetime import datetime
    >>> date = datetime(2023, 12, 25)
    >>> ar_date = convert(date)
    >>> print(ar_date.year)  # 4723
"""

from datetime import datetime
from typing import Final

from arconverter.ardate import ArDate
from arconverter.constants import arDays, arDayShort, arMonths, arShortMonths

MIN_YEAR: Final[int] = 1970  # Unix epoch
MAX_YEAR: Final[int] = 2099  # Upper limit before conversion breaks

YEAR_OFFSET: Final[int] = 2700 # Set by the Absolom Reckoning calendar (Paizo)


class ArConverterError(Exception):
    """Base exception for arconverter errors."""

    pass


def validate_date(date: datetime) -> None:
    """Validate the input date is within acceptable ranges."""
    if not isinstance(date, datetime):
        raise ArConverterError('Input must be a datetime object')

    if date.year < MIN_YEAR or date.year > MAX_YEAR:
        raise ArConverterError(f'Year must be between {MIN_YEAR} and {MAX_YEAR}')


def convert(target_date: datetime) -> ArDate:
    """Convert a given date to Absolom Reconing date."""
    validate_date(target_date)

    try:
        # Break the year up into pieces
        year = target_date.year
        month = target_date.month
        day = target_date.day
        day_of_week = target_date.weekday() + 1

        # Build the resulting arDate and it's properties
        result = ArDate()
        result.year = year + YEAR_OFFSET
        result.monthNum = month
        result.day = day
        result.month = arMonths[month]
        result.monthShort = arShortMonths[month]
        result.weekday = arDays[day_of_week]
        result.weekdayNum = day_of_week
        result.weekdayShort = arDayShort[day_of_week]

        return result

    except KeyError as e:
        raise ArConverterError(f'Invalid calendar mapping: {e}')
    except Exception as e:
        raise ArConverterError(f'Conversion error: {e}')
