from itertools import compress
import re
import arrow


addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

new = [n > 5 for n in counts]

l = list(compress(addresses, new))
print(l)
test = '12   23, 34; 1213'
print(re.split(r'\s*[,;\s]\s*', test))

print(arrow.now().isoformat())
t = arrow.get('2018-12-01 10:23')
print(t.isoformat().split('.')[0])
