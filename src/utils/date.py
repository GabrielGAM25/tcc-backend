import datetime
import calendar


def date_string_to_date(date_string):
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)
