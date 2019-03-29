import re
import os


if __name__ == "__main__":
    s = " hello new world \n"
    # strip用于取出首尾指定字符
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())
    s = "test ?"
    s1 = s.replace('?', 'new')
    print(s1)
    s2 = re.sub('new', 'fresh', s1, flags=re.IGNORECASE)
    print(s2)