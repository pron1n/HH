def strToList(n):
    list = []
    for i in n:
        list.append(i)
    return(list)


for i in range(10, 10000):
    x5 = strToList(str(i * 5))
    x5.sort()
    x6 = strToList(str(i * 6))
    x6.sort()
    if x5 == x6:
        print(i)