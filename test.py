import requests
import re
import json
from collections import defaultdict
import time
import os


if __name__ == "__main__":
    key = "test@@&&404"
    # cmd = 'echo "{}" >> request.log'.format(key)
    # print(cmd)
    # os.system(cmd)
    # f = open('./test.log', 'a+')
    # # f.write("test")
    # for i in range(10):
    #     f.write('test')
    #     print('test')
    #     time.sleep(1)
    # f.close()
    # l = "@@"
    # print(l.strip().split('@@'))
    # data = l.strip().split('@@')
    # print(len(data))
    # print({"": "1"})
    # dct = {"key@200": 21, "lock@200": 123, "lock@404": 134, "key@206": 12, "key@304": 56}
    # print(sorted(dct.items()))
    # data = sorted(dct.items())
    # r = defaultdict(dict)
    # for k, v in data:
    #     l = k.split('@')
    #     key, code = l[0], l[1]
    #     if key not in r.keys():
    #         r[key] = {code: v}
    #     else:
    #         r[key].update({code: v})
    # print(r)
    # l = sorted(r.items(), key=lambda k: sum(k[1].values()), reverse=True)
    # print(l)
    # d = []
    # for k, v in l:
    #     d.append((k, sorted(v.items(), key=lambda k: k[1], reverse=True)))
    # print(d)
        # list1 = sorted(dct.items(), key=lambda k: k[1], reverse=True)
        # print(list1)
        # for k, v in list1:
        #     print(k, v)
    # resp = requests.request('GET', url="https://cn.bing.com")
    # print(resp.status_code)
    # c = '{}'
    # print(json.loads(c))
    # data = [1, 2, '00'*5]
    # print(data)
    # test_data = ['代码', 'merge', 'Merdsge', 'fdMERGE', '合是吗并代码', '冲突解决', '提交代码', '冲当时的']
    # test_res = []
    # for d in test_data:
    #     test_res.append(re.findall(r'merge|Merge|MERGE|合并|冲突', d))
    # print(test_res)
    # print([d.upper() for d in test_data])
    # for t in test_res:
    #     if t:
    #         print(True)
    #     else:
    #         print(False)
    # url = 'http://10.100.51.45/rate/api/delete-test-code'
    # resp = requests.get(url)
    # print("*"*10)
    # print(resp.status_code)
    # print("*"*10)
    # print(min(1, 3, 2))
    # data = [1,3, 4]
    # for i in range(2):
    #     print(data.pop())