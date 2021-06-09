# encoding: utf-8


from node import Node


class LinkedBag(object):
    def __init__(self, sourceCollection=None):
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._items = None

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def __iter__(self):
        cursor = self._items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        # result = ArrayBag(self)
        result = self
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def remove(self, item):
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self_items = self._items.next
        else:
            trailer.next = probe.next


if __name__ == '__main__':
    lyst = [2013, 61, 3, [1001, 1002]]
    ar = LinkedBag(lyst)
    print(len(ar))
    print(ar.isEmpty())
    print(ar)

    ar.add(77)
    print(ar)

    for i in ar:
        print(i, end=' ')
    print('\n')

    ar = ar + [1, 2, 3]
    print(ar)

    ar.remove(3)
    print(ar)

    ar.clear()
    print(ar)
