# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-07 12:18
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test15.py
# ----------------------------------------------


if __name__ == "__main__":
    # filter 方法，func + iterator
    data = [i for i in range(1, 11)]
    print(list(filter(lambda x: x % 2 == 0, data)))
    # 什么是猴子补丁
    # 运行是动态替换模块的方法
    # python 是如何管理内存的，引用计数和分代垃圾回收的机制
    # 当退出 python3 时，是否会释放所有内存分配，答案时否定的，对于循环引用和相互引用的内存还不会释放
