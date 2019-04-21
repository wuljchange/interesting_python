def maopao(data: list):
    for i in range(len(data)):
        for j in range(i+1, len(data)-i):
            if data[i] < data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data


if __name__ == "__main__":
    # data = [5, 3, 1, 2, 4, 5, [12]]
    # # print(maopao(data))
    # # dct = {
    # #     1: 'test',
    # # }
    # # dct[2] = dct[3] = dct[1]
    # # print(dct)
    # print(set(data))
    a = round(round(1.0/3, 5)*1000, 2)
    print(a)