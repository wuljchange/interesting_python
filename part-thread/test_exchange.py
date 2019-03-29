from contextlib import contextmanager
from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


class Task:
    def send(self, msg):
        print(msg)


_changes = defaultdict(Exchange)


def get_change(name):
    return _changes[name]


if __name__ == "__main__":
    data = {'new1': 1, 'new3': 2, 'new2': 3}
    # new = sorted(data.items())
    print(dict(sorted(data.items())))
    # exc = get_change('name')
    # task_a = Task()
    # task_b = Task()
    # with exc.subscribe(task_a, task_b):
    #     exc.send('msg1')
    #     exc.send('msg2')