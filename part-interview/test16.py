# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-07 18:11
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test16.py
# ----------------------------------------------
import re


if __name__ == "__main__":
    # 使用正则表达式匹配地址
    s = "www.baidu.com.jkjh"
    if re.match(r'(.*).(.*).(.*)', s):
        print("pass")
    r = re.findall(r'(.*)\.(.*)\.(.*)', s)
    print(r)
    s = " 98 100 102 "
    s = re.sub(r' (\d+) (\d+) (\d+) ', r'\3/\2/\1', s)
    print(s)
    # 正则匹配中 (.*) 和 (.*?) 的区别是一个是最长匹配，一个是最短匹配
    text = 'Computer says "no." Phone says "yes."'
    t1 = re.findall(r'"(.*)"', text)
    t2 = re.findall(r'"(.*?)"', text)
    print(t1)
    print(t2)
    # 匹配邮箱的正则表达式
    text1 = "test@wulj.com, test2@wulinjiang.com,"
    t3 = re.findall(r'\s*(.*?)@(.*?).com,\s*', text1)
    print(t3)