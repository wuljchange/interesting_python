# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-08 12:13
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test20.py
# ----------------------------------------------
from collections import defaultdict


if __name__ == "__main__":
    # 找出列表中重复的元素
    data = [1, 2, 3, 4, 3, 5, 5, 1]
    dct = defaultdict(list)
    for d in data:
        dct[str(d)].append(d)
    print(dct)
    for k, v in dct.items():
        if len(v) > 1:
            print(k)
    s = "+++--++--"
    print("".join(sorted(s)))