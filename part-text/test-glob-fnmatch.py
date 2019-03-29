import glob
import fnmatch
import os.path


if __name__ == "__main__":
    dir_path = '/root/tmp/test'
    path = '/root/tmp/test/*.py'
    pyfiles = glob.glob(path)
    pyfiles2 = [name for name in os.listdir(dir_path) if fnmatch(name, '*.py')]