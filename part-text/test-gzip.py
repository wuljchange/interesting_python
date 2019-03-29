import gzip
import bz2


if __name__ == "__main__":
    # gzip作用于一个已经打开的二进制文件 new character
    f = open('file.gz', 'rb')
    with gzip.open(f, 'rb') as f:
        print(f.read())
    # with语句结束自动会关闭文件
    with gzip.open('file', 'wt') as f:
        f.read("test")
    print("new line")
    with bz2.open('file', 'wt') as f:
        f.read("test")
    print("end")