from struct import Struct


def record_data(records, format, file):
    record_struct = Struct(format)
    for r in records:
        file.write(record_struct.pack(*r))


def read_data(format, f):
    """
    增量块的形式迭代
    :param format:
    :param f:
    :return:
    """
    read_struct = Struct(format)
    chunks = iter(lambda: f.read(read_struct.size), b'')
    return (read_struct.unpack(chunk) for chunk in chunks)


def unpack_data(format, f):
    """
    全量迭代
    :param format:
    :param f:
    :return:
    """
    unpack_data = Struct(format)
    return (unpack_data.unpack_from(f, offset) for offset in range(0, len(f), unpack_data.size))


if __name__ == "__main__":
    records = [
        (1, 2, 3),
        (2, 3, 4),
        (3, 4, 5),
    ]
    with open('test.file', 'wb') as f:
        record_data(records, '<idd', f)