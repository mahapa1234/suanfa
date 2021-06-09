# encoding: utf-8


def quickSort(listIn):
    def pathSort(lista, sIndex, eIndex):
        flag = lista[eIndex]
        i = sIndex - 1
        for j in range(sIndex, eIndex):
            if lista[j] < flag:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
            else:
                pass
        lista[i+1], lista[eIndex] = lista[eIndex], lista[i+1]
        return i+1

    def qSort(listb, sIndex, eIndex):
        if sIndex >= eIndex:
            return
        else:
            middle = pathSort(listb, sIndex, eIndex)
            qSort(listb, sIndex, middle-1)
            qSort(listb, middle+1, eIndex)
            # print(listb)

    qSort(listIn, 0, len(listIn)-1)
    return listIn


if __name__ == '__main__':
    li = [34, 123, 77, 88, 12, 34, 545, 55]
    print(quickSort(li))
