import numpy as np


if __name__ == "__main__":
    """
    使用numpy模块来对数组进行运算
    """
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x+y)
    print(x*2)
    nx = np.array(x)
    ny = np.array(y)
    print(nx*2)
    print(nx+10)
    print(nx+ny)
    print(np.sqrt(nx))
    print(np.cos(nx))
    # 二维数组操作
    a = np.array([[1, 2, 3], [2, 3, 4]])
    # select row 1
    print(a[1])
    # select column 1
    print(a[:, 1])
    print(np.where(a > 1, a, 0))