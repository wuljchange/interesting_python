import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, priority, item):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    nums = [1, 5, 2, 4, 3]
    a = heapq.nlargest(3, nums)
    print(a)
    b = heapq.nsmallest(3, nums)
    print(b)
    print(type(b))
    # 对集合进行堆排序放入列表中，返回值为 None
    c = heapq.heapify(nums)
    print(c)
    print(nums)
    nums2 = [1, 5, 2, 4, 3]
    # heappop,heappush
    d = heapq.heappop(nums2)
    print(d)
    e = heapq.heappop(nums2)
    print(e)
    print(nums2)
    heapq.heappush(nums2, 1)
    print(nums2)
    f = heapq.heappop(nums2)
    print(f)
    # deque 保留最后插入的 N 个元素，返回值是可迭代对象
    from collections import deque
    q = deque(maxlen=3)
    q.append(1)
    q.appendleft(2)
    print(q)
    q.appendleft(3)
    q.appendleft(4)
    print(q)
    q.append(5)
    print(type(q))
    a, *b, c = q
    print(a, b, c)
    # sorted 排序可迭代对象，通过切片，左闭右开，切记!
    nums3 = [1, 5, 3, 2]
    print(sorted(nums3)[1:])
    # re 模块
    t = 'asdf fjdk; afed, fjek,asdf, foo'
    import re
    # 多个分隔符，不保留分隔符分组
    f1 = re.split(r'[;,\s]\s*', t)
    # 多个分隔符，保留分隔符分组
    f2 = re.split(r'(;|,|\s)\s*', t)
    # 多个分隔符，不保留分隔符分组
    f3 = re.split(r'(?:;|,|\s)\s*', t)
    print(f1)
    print(f2)
    print(f3)
