# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-01 11:28
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test03.py
# ----------------------------------------------
if __name__ == "__main__":
    # 对列表元素去重
    aList = [1, 2, 3, 2, 1]
    b = set(aList)
    print(list(b))
    # 2，太简单 不说了
    s1 = "1,2,3"
    print(s1.split(","))
    # 3，找出两个列表中相同元素和不同元素
    a = [1, 2, 5, 3, 2]
    b = [4, 5, 6, 1, 2]
    common_l = list(set(a) & set(b))
    print(common_l)
    only_in_a = list(set(a) - set(common_l))
    only_in_b = list(set(b) - set(common_l))
    print(only_in_a)
    print(only_in_b)
    # 一行代码展开 list，nice
    a = [[1, 2], [3, 4], [5, 6]]
    b = [j for i in a for j in i]
    print(b)
    # numpy 实现，flatten 方法，然后转换成 list
    import numpy as np
    c = np.array(a).flatten().tolist()
    print(c)
    # 合并列表，list 可以用 extend 方法
    a = [1, 2, 3]
    b = [4, 5, 6]
    a.extend(b)
    print(a)
    # 打乱一个列表
    import random
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print(a)
    print(random.randint(1, 10))