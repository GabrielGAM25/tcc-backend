from random import randrange
from datetime import timedelta


def random_date(start, end):
    days_delta = (end - start).days
    random_number_of_days = randrange(days_delta)

    random_date = start + timedelta(days=random_number_of_days)
    return random_date
