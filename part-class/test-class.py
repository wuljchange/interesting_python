class Structure1:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Excepted {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid arguments {}'.format(','.join(kwargs)))


class Stock(Structure1):
    _fields = ["name", "age", "career"]


class Structure2:
    _fields = ["name", "age", "career"]

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Excepted {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid arguments {}'.format(','.join(kwargs)))


if __name__ == "__main__":
    data = ["test1", "test2", "name"]
    kwargs = {"name": "wulj", "age": 23}
    print(kwargs.keys()-data)
    test_dict = {"name": "value", "test": "new"}
    print(','.join(test_dict))
    s1 = Stock("Alex", 23, "programmer")
    print(s1.name, s1.age, s1.career)
    s2 = Stock("lucy", age=22, career="teacher")
    print(s2)
    s3 = Stock("Mary", 23, "player", "like")
    print(s3)
