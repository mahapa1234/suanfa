# encoding: utf-8


def selectionSort(lyst):
    for i in range(len(lyst)):
        minIndex = i
        for j in range(i+1, len(lyst)):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
        if minIndex != i:
            lyst[i], lyst[minIndex] = lyst[minIndex], lyst[i]

# def selectionSort(lyst):
#     i = 0
#     while i < len(lyst) - 1:
#         minIndex = i
#         j = i + 1
#         while j < len(lyst):
#             if lyst[j] < lyst[minIndex]:
#                 minIndex = j
#             j += 1
#         if minIndex != i:
#             lyst[i], lyst[minIndex] = lyst[minIndex], lyst[i]
#         i += 1


if __name__ == '__main__':
    lyst = [7, 11, 25, 5, 1, 8, 99, 4, 9, 112, 3]
    selectionSort(lyst)
    print(lyst)