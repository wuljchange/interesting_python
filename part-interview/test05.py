# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-01 12:45
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test05.py
# ----------------------------------------------


# 定义一个生成器的函数，需要用到 yield
def my_generate(nums):
    for i in nums:
        yield i


if __name__ == "__main__":
    # 一行代码搞定交换字典的 key value 值
    dct1 = {"A": 1, "B": 2}
    dct2 = {str(v): k for k, v in dct1.items()}
    print(dct2)
    # 实现 tuple 和 list 的转换
    a = (1, 2, 3)
    print(a)
    b = list(a)
    print(b)
    # 把 列表转换成生成器
    c = [i for i in range(3)]
    g = my_generate(c)
    print(g)
    # 遍历生成器
    for i in g:
        print(i, end=" ")
    print("")
    # 编码
    a = "hello"
    b = "你好"
    print(a.encode("utf-8"))
    print(b.encode("utf-8"))