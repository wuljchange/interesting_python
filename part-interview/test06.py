# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-01 13:05
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test06.py
# ----------------------------------------------
import json
from datetime import datetime
from json import JSONEncoder
from functools import wraps


class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ComplexEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return super(ComplexEncoder, self).default(o)


def bb(n: int):
    def multi(args):
        return n*args
    return multi


# 函数定义成装饰器的时候，建议加上 wraps，他能保留装饰器定义函数的原有名称和docstring
def dt(func):
    @wraps(func)
    def new(*args, **kwargs):
        res = func(args)
        return res
    return new


if __name__ == "__main__":
    # 交换两个变量的值，可以直接赋值
    a, b = 1, 2
    print(a, b)
    print(id(a), id(b))
    a, b = b, a
    print(a, b)
    print(id(a), id(b))
    # read，readline，readlines
    # read 是直接读取整个文件内容
    # readline 是读取文件的一行内容，从最开始读起
    # readlines 是读取文件所有内容，按行分隔成 list，会把换行符也带上
    with open('test.txt', 'r') as f:
        # r1 = f.read()
        # print("r1 "+r1)
        # r2 = f.readline()
        # print("r2 "+r2)
        r3 = f.readlines()
        print(r3)
    # json 序列化支持的数据类型有哪些
    # 基本上 python3 的基本数据类型都支持
    d1 = {"d1": 1}
    d2 = {"d2": "2"}
    d3 = {"d3": dict()}
    d4 = {"d4": list()}
    d5 = {"d5": tuple()}
    d6 = {"d6": True}
    print(json.dumps(d1))
    # json 序列化对象支持 datetime 对象，定义一个函数或者类，把 datetime 对象转换成字符串即可
    # 一般自己定义的类是有 self.__dict__ 方法的
    m = Man("test", 24)
    d7 = {"d7": m}
    print(json.dumps(d7, default=lambda obj: obj.__dict__))
    d8 = {"d8": datetime.now()}
    print(json.dumps(d8, cls=ComplexEncoder))
    # json 序列化的时候，遇到中文会默认转换成 unicode，要求让他保留中文格式
    d9 = {"hello": "你好"}
    print(json.dumps(d9))
    print(json.dumps(d9, ensure_ascii=False))
    # 合并文件信息，按顺序排列
    with open('test1.txt', 'r') as f1:
        t1 = f1.read()
    with open('test2.txt', 'r') as f2:
        t2 = f2.read()
    print("t1 ", t1)
    print("t2 ", t2)
    # 字符串属于可迭代对象，sorted 过后返回一个 list
    t = sorted(t1 + t2)
    print("t ", "".join(t))
    # 当前日期计算函数
    dt1 = "20190530"
    import datetime
    dt1 = datetime.datetime.strptime(dt1, "%Y%m%d")
    print(dt1)
    dt2 = dt1 + datetime.timedelta(days=5)
    print(dt2.strftime("%Y%m%d"))
    import arrow
    dt1 = "2019-05-30"
    dt1 = arrow.get(dt1)
    print(dt1)
    dt2 = dt1.shift(days=+5)
    print(dt2.isoformat())
    # 1 行代码实现 1-100 之间的偶数
    # range 方法是左闭右开
    t = [i for i in range(1, 100) if i % 2 == 0]
    print(t)
    # with 语句的作用，用作上下文管理器，一般用于文件读写，方式没有及时关闭文件
    # 如果一个对象有 self.__enter__(self) 和 self.__exit__(self) 方法的话，可以用 with 做上下文管理器
    # python 计算一个文件中大写字母的个数
    with open('test1.txt', 'r') as f:
        t = f.read()
        print(t)
    l = [i for i in t if "A" <= i <= "Z"]
    print(l)
    print(len(l))