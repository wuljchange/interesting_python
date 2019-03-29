from collections import defaultdict

counter_words = defaultdict(list)


# 定位文件中的每一行出现某个字符串的次数
def locate_word(test_file):
    with open(test_file, 'r') as f:
        lines = f.readlines()
    for num, line in enumerate(lines, 1):
        for word in line.split():
            counter_words[word].append(num)
    return counter_words


if __name__ == "__main__":
    file = 'data/test.txt'
    ret = locate_word(file)
    print(ret.get('test', []))
