import os.path
import time
import glob
import fnmatch


if __name__ == "__main__":
    dir_path = '/data/proc/log'
    file_name = [name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))]
    dir_name = [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]
    pyfile = [name for name in os.listdir(dir_path) if name.endswith('.py')]
    path = '/data/prolog/log/test.log'
    print(os.path.basename(path))
    print(os.path.dirname(path))
    print(os.path.split(path))
    print(os.path.join('root', 'tmp', os.path.basename(path)))
    # 测试文件或者目录是否存在 指定类型判断
    if os.path.exists(path):
        print(True)
    os.path.isfile(path)
    os.path.isdir(path)
    # 测试是否是软连接
    os.path.islink(path)
    # 得到软连接的完整路径
    os.path.realpath(path)
    os.path.getsize(path)
    # 得到文件的创建时间
    os.path.getmtime(path)
    # 修改文件的创建时间
    time.ctime(os.path.getmtime(path))