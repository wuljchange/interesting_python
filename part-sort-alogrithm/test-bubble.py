# 冒泡排序 该算法的事件复杂度未O(N^2)
# 具体过程如下 首先遍历数组中的n个元素，对数组中的相邻元素进行比较，如果左边的元素大于右边的元素，则交换两个元素所在的
# 位置，至此，数组的最右端的元素变成最大的元素，接着对剩下的n-1个元素执行相同的操作。


def bubble_sort(data: list):
    # 外面的循环控制内部循环排序的次数，例如5个数，只需要4次排序就行了
    for i in range(len(data)-1):
        change = False
        # 内部循环比较相邻元素，找到剩下元素的最大值放在数组的右边
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                change = True
        # 当change=False时，说明没有交换的情况发生，说明该数组已经排序完成
        # 减少了循环的次数
        if not change:
            break
    return data


if __name__ == "__main__":
    t_data = [5, 4, 3, 2, 1]
    print(bubble_sort(t_data))