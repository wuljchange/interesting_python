from collections import Iterable
import heapq


# 处理嵌套列表
def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 10, 9]
    l2 = [2, 3, 4, 5, 8, 6, 11]
    for i in heapq.merge(l1, l2):
        print(i)
    print("end")
    items = [1, 2, 3, [2, 3, 4], [5, 6, 7]]
    for i in flatten(items):
        print(i)
    # 改变输出的分割符和行尾符
    print(1, 2, sep=' ', end='#\n')
    # str.join()只能连接字符串，非字符串的需要用sep方式隔开
    d = ["wulj", 1, 2]
    print(*d, sep=',')