# encoding: utf-8


def indexOfMin(lyst):
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[minIndex] > lyst[currentIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex


if __name__ == '__main__':
    lyst = [7, 11, 25, 5, 1, 8, 99, 4, 9, 112, 3]
    print(indexOfMin(lyst))
    print(lyst[indexOfMin(lyst)])

