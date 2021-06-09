# 插入排序
# encoding: utf-8

li = [34, 123, 77, 88, 12, 34, 545]


def inserSort(listIn):
    for i in range(1, len(listIn)):
        j = i
        while(j>=1):
            if listIn[j] < listIn[j-1]:
                listIn[j], listIn[j-1] = listIn[j-1], listIn[j]
            else:
                break
            j -= 1
    return listIn


if __name__ == '__main__':
    out = inserSort(li)
    print(out)
