import datetime
import random


def random_date(start, l):
    current = start
    while l >= 0:
        random_minutes = random.randint(1, 60)
        random_days = random.randint(1, 30)
        curr = current + \
            datetime.timedelta(days=random_days, minutes=random_minutes)
        yield curr
        l -= 1


# startdate = datetime.datetime(2024, 3, 6)
# for x in reversed(list(random_date(startdate, 10))):
#     print(x.strftime("%d/%m/%y %H:%M"))

r = random.choices([11, 34, 43, 53, 23, 54], k=4)
print(r)
random.shuffle(r)
print(r)
