# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-08 11:30
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test19.py
# ----------------------------------------------
# 单例模式的 N 种实现方法，就是程序在不同位置都可以且仅可以取到同一个实例


# 函数装饰器实现
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            # cls 作为 key，value 值为 cls 的实例化
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Cls(object):
    def __init__(self):
        print("__init__")


# 类装饰器实现
class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls2:
    def __init__(self):
        print("__init__2")


# 使用 new 关键字实现单例模式
class Singleton1(object):
    # 类属性，公共属性
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print("__init__3")


# 使用 metaclass 实现单例模式
class Singleton3(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton3, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Singleton4(metaclass=Singleton3):
    def __init__(self):
        print("__init__4")


if __name__ == "__main__":
    c = Cls()
    d = Cls()
    print(id(c) == id(d))
    e = Cls2()
    f = Cls2()
    print(id(e) == id(f))
    g = Singleton1()
    h = Singleton1()
    print(id(g) == id(h))
    i = Singleton4()
    j = Singleton4()
    print(id(i) == id(j))