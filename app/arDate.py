class arDate:
    '''Absalom Reckoning Date'''

    month: str
    day: int
    year: int
    weekday: str
    weekdayNum: int
    monthNum: int
    monthShort: str
    monthLong: str

    def shortDate(self) -> str:
        '''Returns a short date string'''
        return f"{self.monthShort} {self.day}, {self.year}"

    def longDate(self) -> str:
        '''Returns a long date string'''
        return f"{self.monthLong} {self.day}, {self.year}"

    def weekdayDate(self) -> str:
        '''Returns a weekday date string'''
        return f"{self.weekday} {self.monthLong} {self.day}, {self.year}"

    def __str__(self) -> str:
        '''Returns a short date string'''
        return self.shortDate()
