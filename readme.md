# Absalom Reckoning Converter
![Python Version](https://img.shields.io/pypi/pyversions/arconverter)
![PyPI version](https://img.shields.io/pypi/v/arconverter)
![License](https://img.shields.io/pypi/l/arconverter)
![Downloads](https://img.shields.io/pypi/dm/arconverter)
w
Evan Young 2025

## Copyright Note
This library uses trademarks and/or copyrights owned by Paizo Inc., used under Paizo's Fan Content Policy (paizo.com/licenses/fancontent). This library is not published, endorsed, or specifically approved by Paizo. For more information about Paizo Inc. and Paizo products, visit paizo.com.

## Project Description
The `Absalom Reckoning` is a calendar used in the Pathfinder Roleplaying Game.
A quick little project that I am making into my first deployed package on pypi. It converts standard dates into the Absalom Reconing Calendar used in the Pathfinder Roleplaying Game.

## ArDate Attributes
- `month`: Full month name in AR calendar (e.g. "Erastus")
- `monthShort`: Abbreviated month name (e.g. "Era")
- `commonMonth`: Common folk month name (e.g. "Fletch")
- `day`: Day of the month (1-31)
- `year`: Year in AR calendar
- `weekday`: Full weekday name (e.g. "Moonday")
- `weekdayShort`: Abbreviated weekday name (e.g. "Moon")
- `weekdayNum`: Day of week number (1-7, starts with Moonday)
- `monthNum`: Month number (1-12)
- `season`: Current season (Winter, Spring, Summer, Fall)

## Methods
- `convert()`: Converts a datetime object into an ArDate object
- `short_date()`: Returns date in format "Era 10, 4723"
- `long_date()`: Returns date in format "Erastus 10, 4723"
- `weekday_date()`: Returns date in format "Moonday Erastus 10, 4723"
- `common_long_month()`: Returns date with common month in format "Fletch 10, 4723"
- `month_season()`: Returns current season as string

## Installation
```powershell
pip install arconverter
```
*Or your preferred method of installing python packages.*

## Useage
```python
from datetime import datetime
from arconverter import convert

# Convert a date to Absalom Reckoning
ar_date = convert(datetime(2023, 7, 10))

# Print the date in various formats
print(ar_date.long_date())        # "Erastus 10, 4723"
print(ar_date.short_date())       # "Era 10, 4723"
print(ar_date.weekday_date())     # "Moonday Erastus 10, 4723"
print(ar_date.common_long_month())# "Fletch 10, 4723"
print(ar_date.month_season())     # "Summer"
```

&Omega;