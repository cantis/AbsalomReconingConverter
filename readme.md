# Absalom Reckoning Converter

## Copyright Note
Note: Absalom Reckoning is a calendar used in the Pathfinder Roleplaying Game. Pathfinder is a registered trademark of Paizo Inc., and the Pathfinder Roleplaying Game and the Pathfinder Roleplaying Game Compatibility Logo are trademarks of Paizo Inc., and are used under the Pathfinder Roleplaying Game Compatibility License. See http://paizo.com/pathfinderRPG/compatibility for more information on the compatibility license. No infringment is intended.

## Project Description
A quick little project that I may make into a package. It converts standard dates into the Absalom Reconing calendar used in the Pathfinder Roleplaying Game.

There is a convert method that does the date conversion and returns an arDate object.

The arDate object has a __str__ method that returns the date in the format of "{short month} {day}, {year}".

### arDate methods
shortDate() - returns the date in the format of "{short month} {day}, {year}"
longDate() - returns the date in the format of "{long month} {day}, {year}"
weekdayDate() - returns the date in the format of "{weekday} {long month} {day}, {year}"

### arDate attributes
year - the year in the Absalom Reckoning calendar
month - the long name of the month
day - the day of the month (int)
year - the year in the Absalom Reckoning calendar (+2k from standard)
weekday - the long name of the weekday
weekdayShort - the short name of the weekday
weekdayNum - the number of the weekday (int)
monthNum - the number of the month (int)
monthShort - the short name of the month

## Command line usage
```powershell
PS python
>>> import arConverter
>>> arConverter.convert("2023-07-02")
>>> Sunday Erastus 2, 4723
```

## Future
Adding a seasonal indicator to the date. This will be a string that will be one of the following: "Spring", "Summer", "Fall", "Winter".
