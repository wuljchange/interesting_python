# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-08 11:05
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test18.py
# ----------------------------------------------


def search_2(data, l):
    """ 二分查找法 """
    length = len(l)
    # 递归一定要写出退出条件
    if length <= 1:
        if length <= 0:
            return False
        elif data == l[0]:
            return 0, l[0]
        else:
            return False
    mid_index = int(length/2)
    mid = l[mid_index]
    if data > mid:
        f_index = mid_index + 1
        return search_2(data, l[f_index:])
    elif data < mid:
        return search_2(data, l[:mid_index])
    else:
        return mid_index, mid


if __name__ == "__main__":
    data = 0
    l = [i for i in range(10)]
    if search_2(data, l):
        index, value = search_2(data, l)
        print(index, value)
    else:
        print(False)
