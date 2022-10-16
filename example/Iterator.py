"""
Iterator
迭代器模式（Iterator）实际上在Python的集合类中已经广泛使用了。

"""


class Iterator:
    def __init__(self, max: int = 100, *, first: int = 0) -> None:
        self._first = first
        self._current = self._first
        self.max = max

    def __iter__(self,):
        return self

    def __next__(self,):
        self._current += 1
        self.is_done()
        return self._current-1

    def first(self):
        return self._first

    def current_item(self):
        return self._current

    def is_done(self):
        if self._current > self.max:
            raise StopIteration


if __name__ == '__main__':
    iterator = Iterator(max=100)
    print(iterator.current_item())
    iterator.__next__()
    print(iterator.current_item())

    for i in Iterator(100):
        print(i)
