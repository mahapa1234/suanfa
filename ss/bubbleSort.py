# encoding: utf-8


def bubbleSort(lyst):
    for i in range(len(lyst)-1):
        for j in range(1, len(lyst)-i):
            if lyst[j] < lyst[j-1]:
                lyst[j], lyst[j-1] = lyst[j-1], lyst[j]


# def bubbleSort(lyst):
#     n = len(lyst)
#     while n > 1:
#         i = 1
#         while i < n:
#             if lyst[i] < lyst[i-1]:
#                    lyst[i], lyst[i-1] = lyst[i-1], lyst[i]
#             i += 1
#         n -= 1


if __name__ == '__main__':
    lyst = [7, 11, 25, 5, 1, 8, 99, 4, 9, 112, 3]
    bubbleSort(lyst)
    print(lyst)