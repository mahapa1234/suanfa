# encoding: utf-8


def sequentialSearch(target, lyst):
    """ Return the position of the target item in found """
    position = 0
    while position < len(lyst):
        if lyst[position] == target:
            return position
        position += 1
    return -1


if __name__ == '__main__':
    lyst = [7, 11, 25, 5, 1, 8, 99, 4, 9, 112, 3]
    print(sequentialSearch(88, lyst))
    print(sequentialSearch(4, lyst))
