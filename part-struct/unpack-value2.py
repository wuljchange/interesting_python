records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4),
           ]


def drop_first_last(grades):
    _, *middle, _ = grades
    return middle


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


if __name__ == "__main__":
    for tag, *args in records:
        print(args)
        print(*args)
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)
    print("done")