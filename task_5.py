def strToList(n):
    list = []
    for i in n:
        list.append(i)
    return (list)


def isPol(list):
    list1 = []
    for i in list:
        list1.append(i)
    list.reverse()
    if list == list1:
        return True
    else:
        return False


k = 0
for i in range(1, 13592):
    c = 0
    curstr = str(i)
    while isPol(strToList(curstr)) == False:
        curint = int(curstr)
        curint += int("".join(strToList(curstr).reverse()))
        curstr = str(curint)
        c += 1
        if c == 51:
            k += 1
            break

print(k)