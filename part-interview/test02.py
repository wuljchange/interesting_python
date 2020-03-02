# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-01 10:39
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test02.py
# ----------------------------------------------
if __name__ == "__main__":
    # gbk 和 utf-8 格式之间的转换
    # gbk 编码，针对于中文字符
    t1 = "中国加油"
    t1_gbk = t1.encode("gbk")
    print(t1.encode("gbk"))
    # utf-8 字符
    t2_utf = t1_gbk.decode("gbk").encode("utf-8")
    print(t2_utf)
    print(t1.encode("utf-8"))
    # 正则切分字符串
    s1 = "info :  xiaoZhang 33 shandong"
    import re
    # 非捕获分组
    c1 = re.compile(r'\s*[:\s]\s*')
    l1 = re.split(c1, s1)
    print(l1)
    # 捕获分组
    c2 = re.compile(r'(\s*:\s*|\s)')
    l2 = re.split(c2, s1)
    print(l2)
    # 如果仍需使用圆括号输出非捕获分组的话
    c3 = re.compile(r'(?:\s*:\s*|\s)')
    l3 = re.split(c3, s1)
    print(l3)
    # 去除多余空格
    a = "你好 中国 "
    a = a.rstrip()
    print(a)
    # 字符串转换成小写
    b = "sdsHOJOK"
    print(b.lower())
    # 单引号 双引号 三引号的区别
    # 单引号 和 双引号 输出结果一样，都显示转义后的字符
    a = '-\t-\\-\'-%-/-\n'
    b = "-\t-\\-\'-%-/-\n"
    print(a)
    print(b)
    c = r"-\t-\\-\'-%-/-\n"
    print(c)