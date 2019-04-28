# 插入排序 时间复杂度O(N^2)
# 具体过程如下 每次循环往已经排好序的数组从后往前插入一个元素，第一趟比较两个元素的大小，第二趟插入元素
# 与前两个元素进行比较，放到合适的位置，以此类推。


def insert_sort(data: list):
    for i in range(1, len(data)):
        key = data[i]
        # 相当于相邻元素进行比较，但是逻辑更清楚一点
        for j in range(i-1, -1, -1):
            if data[j] > key:
                data[j+1] = data[j]
                data[j] = key
    return data


if __name__ == "__main__":
    t_data = [2, 4, 1, 5, 3, 5, 9, 10, 8, 7]
    print(insert_sort(t_data))