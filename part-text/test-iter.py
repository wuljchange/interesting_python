from itertools import dropwhile, islice
from itertools import permutations, combinations
from itertools import combinations_with_replacement


def parser(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            print(lineno, line)
            fields = line.split()
            try:
                count = float(fields[0])
            except ValueError as e:
                print('Lineno {} parser {}'.format(lineno, e))


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [2, 3, 4, 5]
    a = [(x, y) for x, y in zip(l1, l2)]
    print(a)
    for index, (x, y) in enumerate(a):
        print(index, x, y)
    line_text = 'test new world'
    print(line_text.split())
    items = [1, 2, 3, 4]
    for i in enumerate(items):
        print(i)
    # 指定行号
    for i in enumerate(items, 2):
        print(i)
    # 允许同一个元素被选取，在一个元祖中
    cp = [i for i in combinations_with_replacement(items, 2)]
    p_test = [i for i in permutations(items, 2)]
    c_test = [i for i in combinations(items, 2)]
    print(p_test)
    print(c_test)
    print(cp)
    with open('../data-struct-algorithm/tmp/test') as f:
        r = f.readlines()
        print(r)
        st = ['#new', '#test', 'test']
        s = islice(st, 1, None)
        for s1 in s:
            print(s1)
        print(s)
        ret = list(filter(lambda x: x.startswith('#'), r))
        print(ret)
        for line in dropwhile(lambda x: x.startswith("#"), f):
            print(line, end=" ")