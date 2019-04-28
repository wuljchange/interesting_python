# 使用lambda对list排序，正数在前，从小到大，负数在后，从大到小
# lambda设置2个条件，先将小于0的排在后面，再对每一部分绝对值排序
data = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
a = sorted(data, key=lambda x: (x < 0, abs(x)))
print(a)