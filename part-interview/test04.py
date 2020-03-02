# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-01 12:33
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test04.py
# ----------------------------------------------
if __name__ == "__main__":
    # 字典操作
    dct = {"a": 1, "b": 2}
    a = dct.pop("a")
    print(a)
    print(dct)
    del dct["b"]
    print(dct)
    # 合并两个字典
    a = {"a": 1, "b": 2}
    b = {"c": 3, "d": 4}
    a.update(b)
    print(a)
    # 生成器的方式生成一个字典，dict 直接初始化 必须是元组的 list 形式才可以
    values = [1, 2, 3]
    keys = ["a", "b", "c"]
    dct = {k: v for k, v in zip(keys, values)}
    print(dct)
    dct2 = dict(zip(keys, values))
    dct3 = dict([("a", 1), ("b", 2)])
    print(dct2)
    print(dct3)