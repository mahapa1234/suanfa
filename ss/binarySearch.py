# encoding: utf-8


def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right)//2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


if __name__ == '__main__':
    lyst = [3, 5, 7, 11, 18, 22, 99, 112, 223, 1111, 2222]
    print(len(lyst))
    print(binarySearch(2222, lyst))
    print(binarySearch(222, lyst))
