# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-04 23:48
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test11.py
# ----------------------------------------------


class Demo:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __call__(self, *args, **kwargs):
        """ 改变实例的状态 """
        self.x, self.y = args


class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@Counter
def foo(name):
    print(name)


class Test:
    # 静态属性
    x = 1
    y = 2

    def __init__(self, x=7, y=8):
        # 成员属性
        self.x = x
        self.y = y

    def normal_func(self):
        print("normal", self.x, self.y)

    @staticmethod
    def static_func():
        print("static", Test().x, Test().y)
        print(Test(3, 4).normal_func())

    @classmethod
    def class_func(cls):
        print("class", Test.x, Test.y)
        print(cls(5, 6).normal_func())


if __name__ == "__main__":
    data = "sastfftsasdsh"
    print(5/2)
    q = [True if x % 3 == 0 else -x for x in range(1, 101)]
    d = [True if data[i] == data[len(data)-i-1] else False for i in range(int(len(data)/2))]
    print(d)

    # 装饰器有什么作用
    # 用于给给现有函数增加额外功能，接收一个函数作为参数
    # 定义的装饰器函数可以带参数，函数本身也可以带参数

    # python 垃圾回收机制
    # 1. 引用计数器回收，引用计数器为0时，就会被解释器的 gc 回收
    # 2. 分代垃圾回收机制，对于对象的相互引用和循环引用，第一种回收方式时无法实现的，具体分为第一代，第二代，第三代
    # 第一代主要用于去除同一代中的相互索引和循环索引，存活的对象放入第二代，以此类推。

    # __call__ 使用
    # 可调用对象，对于类，函数，但凡是可以把()应用到一个对象上的情况都是可调用对象
    # 如果一个类中实现了 __call__ 函数，就可以将一个实例对象变成一个可调用对象
    demo = Demo(1, 2, 3)
    print(demo.x, demo.y)
    # 将实例对象当成函数调用，直接调用类中定义的 __call__ 函数，用于改变对象状态最直接优雅的方法
    demo(5, 6)
    print(demo.x, demo.y)

    for i in range(10):
        foo(i)
    print(foo.count)

    # 判断一个对象是函数还是方法
    # 与类和实例无绑定关系的function都是函数
    # 与类和实例有绑定关系的function都是方法

    # @staticmethod 和 @classmethod
    # @staticmethod 静态方法，与类和实例无关
    # @classmethod 类方法

    Test.static_func()
    Test.class_func()
    Test.x = 10
    t = Test(1, 2)
    print(t.x)
    print(Test.x)
