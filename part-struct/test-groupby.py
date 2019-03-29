from operator import itemgetter
from itertools import groupby


data = [
    {"date": 2019},
    {"date": 2018},
    {"date": 2020}
]
data.sort(key=itemgetter('date'))
print(data)
for date, item in groupby(data, key=itemgetter('date')):
    print(date)
    print(item)
    for i in item:
        print(type(i), i)