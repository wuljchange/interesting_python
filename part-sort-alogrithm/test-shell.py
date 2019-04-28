# 希尔排序 时间复杂度是O(NlogN)
# 又称缩小增量排序


def shell_sort(data: list):
    n = len(data)
    gap = int(n / 2)
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