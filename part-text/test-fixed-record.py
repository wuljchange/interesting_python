from functools import partial


# 从指定文件按固定大小迭代
with open('file', 'rb') as f:
    re_size = 32
    records = iter(partial(f.read, re_size), b'')
    for r in records:
        print(r)