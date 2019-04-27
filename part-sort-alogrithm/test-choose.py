# 选择排序 时间复杂度时O(N^2)
# 具体过程如下 首先在n个元素的数组中找到最小值放在数组的最左端，然后在剩下的n-1个元素中找到最小值放在左边第二个位置
# 以此类推，直到所有元素的顺序都已经确定


def choose(data: list):
    # 外部循环只需遍历n-1次
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data


if __name__ == "__main__":
    t_data = [5, 4, 3, 2, 1]
    print(choose(t_data))