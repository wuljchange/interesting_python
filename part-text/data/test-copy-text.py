from collections import OrderedDict


def dedupe(items):
    """
    删除一个迭代器中重复的元素，并保持顺序
    :param items: 迭代器
    :return:
    """
    a = set()
    for item in items:
        if item not in a:
            yield item
        a.add(item)


# 找出一个字符串中最长的没有重复字符的字段
def cutout(test: str):
    max_data = []
    for s in test:
        if s not in max_data:
            max_data.append(s)
        else:
            yield max_data
            max_data = []
            max_data.append(s)
    yield max_data


if __name__ == "__main__":
    data = [1, 2, 2, 1, 4, 5, 4]
    print(list(dedupe(data)))

    # 简单方法
    order_dct = OrderedDict()
    for item in data:
        order_dct[item] = item
    print(list(order_dct.keys()))
    data = 'anmninminuc'
    for item in cutout(data):
        print(''.join(item))

    output = ''.join(max(cutout(data), key=lambda s: len(s)))
    print(output)