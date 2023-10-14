'''Absalom Reckoning Date Class'''

class ArDate:
    '''Represents an Absalom Reckoning Date'''

    month: str
    day: int
    year: int
    weekday: str
    weekdayShort: str
    weekdayNum: int
    monthNum: int
    monthShort: str

    def short_date(self) -> str:
        '''Returns a short date string'''
        return f"{self.monthShort} {self.day}, {self.year}"

    def long_date(self) -> str:
        '''Returns a long date string'''
        return f"{self.month} {self.day}, {self.year}"

    def weekday_date(self) -> str:
        '''Returns a weekday date string'''
        return f"{self.weekday} {self.month} {self.day}, {self.year}"

    def __str__(self) -> str:
        '''Returns a short date string'''
        return self.short_date()
