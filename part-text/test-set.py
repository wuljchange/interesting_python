if __name__ == "__main__":
    # list,dict,set是不可hash的
    # int,float,str,tuple是可以hash的
    data = [1, 2, '232', (2, 3)]
    data1 = [2, 3, '213', (2, 3)]

    # 两个list取补集，元素在data中，不在data1中
    diff_list = list(set(data).difference(set(data1)))
    print(diff_list)

    # 取交集
    inter_list = list(set(data).intersection(set(data1)))
    print(inter_list)

    # 取并集
    union_list = list(set(data).union(set(data1)))
    print(union_list)