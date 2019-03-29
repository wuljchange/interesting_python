def async_apply(func, args, *, callback):
    result = func(*args)
    callback(result)


def make_handle():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] result is {}'.format(sequence, result))


if __name__ == "__main__":
    # 协程处理
    handle = make_handle()
    next(handle)
    add = lambda x, y: x+y
    async_apply(add, (2, 3), callback=handle.send)
    async_apply(add, (3, 4), callback=handle.send)