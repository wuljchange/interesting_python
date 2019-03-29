import collections
import bisect


class ItemSequence(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    # bisect 插入item到有序队列里，并按照顺序排列
    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == "__main__":
    test = ItemSequence([1, 2, 3])