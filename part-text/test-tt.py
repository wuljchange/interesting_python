from collections import Counter, defaultdict
import requests
import arrow


class Data:
    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    url = 'http://10.100.51.45/rate/repair?start={}&end={}'
    start = '2019-04-01 23:10'
    end = '2019-04-07 23:10'
    ret = requests.get(url.format(start, end))
    print(ret.status_code)
    # dct = {}
    # d = Data('1')
    # dct['re'] = d
    # print(dct)
    # test = defaultdict()
    # data = [{'key1': 1}, {'key2': 2}]
    # for d in data:
    #     test.update(d)
    # print(test)
    # dct = {'data': test}
    # for k, v in dct.items():
    #     print(k)
    #     for k1, v1 in v.items():
    #         print(k1)
    #         print(v1)
    # data = [1, 2, 3, 5, 5]
    # data2 = [2, 3, 4, 6, 2]
    # a = set(d for d in data)
    # print(a)
    # b = set(d for d in data2)
    # print(b)
    # print(a & b)
    # print(a - (a & b))
    # t = tuple(d for d in data)
    # for i in t:
    #     print(i)
    # print(tuple(d for d in data))
    # link = 'http://jira.op.ksyun.com/browse/BIGDATA-614/test'
    # print(link.split('/')[-2])
    # print('http'.upper())
    # for dct in data:
    #     for key in ('key1', 'key2'):
    #         if key not in dct.keys():
    #             dct[key] = 0
    # print(data)
    # ret = defaultdict(Counter)
    # data1 = {'name': {'key1': [1, 2, 3]}}
    # data2 = {'name': {'key1': [2, 3, 4]}}
    # for d in (data1, data2):
    #     for name, data in d.items():
    #         ret[name] += Counter(data)
    # print(ret)