# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-07 18:46
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test17.py
# ----------------------------------------------


def test():
    # 在函数内部使用 global 声名全局变量
    global A
    A = 1
    print(A)


if __name__ == "__main__":
    # input 函数与用户交互使用

    # 解释一下 python 中 pass 的作用。
    # 是空语句，是为了保持程序结构的完整性。不做任何事情，一般用做占位语句。

    # is == 的区别，== 是比较两个对象的 value 值是否相等，is 判断两个对象的 id 是否相等
    # python 对象包含3个基本要素，value id type

    # python 中的作用域，global，nonlocal 语句，全局作用域，在函数内部对函数外部的非全局变量的使用

    # 三元运算符的用法
    b = "1"
    a = "0" if b == "0" else "1"
    print(a)
    # enumerate 模块，遍历会带上索引
    for i, v in enumerate(range(1, 11)):
        print(i, v)
    # python 中的标准模块，functools collections logging
    test()
    A = 2
    print(A)
    # 断言成功继续往下执行，失败就报异常信息
    assert 1 == 1
    print("end")
    # dir 用于查看对象的 属性和方法
    a = [1, 2, [1, 2]]
    b = a
    import copy
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a[2].append(3)
    print(a, b , c, d)
    data = [1, 2, 3, 4]
    print(data[::-1])
    d = [1, 2, 3, 4]
    e = d
    print(id(d), id(e))