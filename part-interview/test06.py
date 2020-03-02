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
