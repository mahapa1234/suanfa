# encoding: utf-8


class Array(object):
    """ Represents an array. """

    def __init__(self, capacity, fillValue=None):
        self._item = list()
        for count in range(capacity):
            self._item.append(fillValue)

    def __len__(self):
        return len(self._item)

    def __str__(self):
        return str(self._item)

    def __iter__(self):
        return iter(self._item)

    def __getitem__(self, index):
        return self._item[index]

    def __setitem__(self, index, newItem):
        self._item[index] = newItem


if __name__ == '__main__':
    a = Array(5)
    print(len(a))
    print(a)
    for i in range(len(a)):
        a[i] = i + 1
    a[0] = 9
    print(a)
    for item in a:
        print(item)
