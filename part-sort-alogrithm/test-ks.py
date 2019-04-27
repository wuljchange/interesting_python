# 快速排序 时间复杂度时O(NlogN)
# 具体过程如下 采用一种分治递归的算法 从数组中任意选择一个数作为基准值，然后将数组中比基准值小的放在左边
# 比基准值大的放在右边，然后对左右两边的数使用递归的方法排序


def partition(data, start, end):
    i = start - 1
    for j in range(start, end):
        # 刚开始以data[end]的值作为基准值
        if data[j] < data[end]:
            i += 1
            # 如果j所在的位置的值小于end,则i往前进一步，并与j的值交换，即将一个新的值加入到小于end的区域
            data[i], data[j] = data[j], data[i]
    i += 1
    data[i], data[end] = data[end], data[i]
    return i


def ks(data: list, start, end):
    if start < end:
        mid = partition(data, start, end)
        ks(data, start, mid-1)
        ks(data, mid+1, end)
    return data


if __name__ == "__main__":
    t_data = [5, 4, 3, 2, 1]
    print(ks(t_data, 0, 4))