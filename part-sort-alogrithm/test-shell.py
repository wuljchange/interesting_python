# 希尔排序 时间复杂度是O(NlogN)
# 又称缩小增量排序 首先设置一个基础增量d，对每间隔d的元素分组，然后对每个分组的元素进行直接插入排序
# 然后缩小增量，用同样的方法，直到增量小于0时，排序完成


def shell_sort(data: list):
    n = len(data)
    gap = int(n / 2)  # 设置基础增量
    # 当增量小于0时，排序完成
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and data[j-gap] > data[j]:
                data[j-gap], data[j] = data[j], data[j-gap]
                j -= gap
        gap = int(gap / 2)
    return data


if __name__ == "__main__":
    t_data = [3, 2, 5, 4, 1]
    print(shell_sort(t_data))