import datetime

def is_13th_friday(month, year):
    try:
        date = datetime.date(year, month, 13)
        return date.weekday() == 4
    except ValueError:
        return False

month = 9
year = 2023
result = is_13th_friday(month, year)
print(result)
