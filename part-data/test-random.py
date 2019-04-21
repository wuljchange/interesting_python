import random


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    # 随机选取一个元素
    print(random.choice(values))
    # 随机选取几个元素且不重复
    print(random.sample(values, 3))
    # 打乱原序列中的顺序
    print(random.shuffle(values))
    # 生成随机整数，包括边界值
    print(random.randint(0, 10))
    # 生成0-1的小数
    print(random.random())
    # 获取N位随机数的整数
    print(random.getrandbits(10))