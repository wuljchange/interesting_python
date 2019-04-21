if __name__ == "__main__":
    x = 1234
    # 函数形式
    print(bin(x))
    print(oct(x))
    print(hex(x))
    # format形式，没有前缀 0b,0o,0x
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))
    #将进制的数据转换成整数字符串
    a = format(x, 'b')
    b = format(x, 'x')
    print(int(a, 2))
    print(int(b, 16))