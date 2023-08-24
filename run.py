from datetime import date

from arConverter.src.arConverter import convert

def main():
    targetDate = date.today()
    arDate = convert(targetDate)
    print(arDate.weekdayDate())

if __name__ == "__main__":
    targetDate = date.today()
    arDate = convert(targetDate)
    print(arDate.weekdayDate())