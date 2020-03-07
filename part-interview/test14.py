# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-06 10:58
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test14.py
# ----------------------------------------------


class Demo(object):
    # 类的属性
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("__init__ 方法被执行")

    def __new__(cls, *args, **kwargs):
        print("__new__ 方法被执行")
        # 调用 cls 类才会执行 __init__ 方法
        return object.__new__(cls)

    def __str__(self):
        return "str test"

    def __repr__(self):
        return "repr test"

    def __del__(self):
        print("del")

    def __getattribute__(self, item):
        # 属性访问拦截器
        if item == "x":
            return "redirect x"
        else:
            return object.__getattribute__(self, item)

    def __call__(self, *args, **kwargs):
        self.x, self.y = args
        print("__call__")


def test(a):
    print(a)
    print(id(a))


if __name__ == "__main__":
    # 列举你所知道的 python 的魔法方法及用途
    # python 有一些内置定义好的方法，这些方法在特定的时期会被自动调用
    # __init__ 函数，创建实例化对象为其赋值使用，是在 __new__ 之后使用，没有返回值
    # __new__ 是实例的构造函数，返回一个实例对象，__init__ 负责实例初始化操作，必须有返回值，返回一个实例对象
    d = Demo(1, 2)
    print(d)
    print(d.x)
    print(d.y)
    # 获取指定类的所有父类
    print(Demo.__bases__)
    d(3, 4)
    print(d.x)
    print(d.y)
    # print(type(d))
    # # 获取已知对象的类
    # print(d.__class__)
    # type 用于查看 python 对象类型
    print(type(d))
    # 对于可变数据类型和不可变数据类型有差异，可变数据类型用引用传参，不可变数据类型用传值
    # 不可变数据类型包括，数字，字符串，元组
    # 可变数据类型包括，列表，字典，集合
    a = 1
    print(a)
    print(id(a))
    test(a)

    a = [1, 2]
    print(a)
    print(id(a))
    test(a)

    a = {1, 2}
    print(a)
    print(id(a))
    test(a)

    # 简述 any()，all() 方法
    # any 数组中的所有元素只要有一个为 True 就返回 True
    if any([True, False]):
        print("any")
    # all 数组中的所有元素只要有一个为 False 就返回 False
    if all([True, False]):
        print("all")
    else:
        print("not all")



