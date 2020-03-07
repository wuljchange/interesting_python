# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-05 20:43
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test13.py
# ----------------------------------------------
import test10


if __name__ == "__main__":
    # python3 高级特性，反射
    # 字符串返回映射到代码的一种机制，python3 提供了四个内置函数 getattr setattr hasattr delattr
    obj = getattr(test10, "acquire_lock")
    if hasattr(test10, "acquire_lock"):
        print("test")
    else:
        print("new")

    # metaclass 作用以及应用场景
    # 元类是一个创建类的类
