from datetime import date

from app.src.arConverter import convert

if __name__ == "__main__":
    targetDate = date.today()
    arDate = convert(targetDate)
    print(arDate.weekdayDate())