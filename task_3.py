def strToList(n):
    list = []
    for i in n:
        list.append(i)
    return(list)

def isPol(list):
    list1 = []
    for i in list:
        list1.append(i)
    list.reverse()
    if list == list1:
        print("is pol")
    else:
        print("no")

while True:
    n = str(input('number: '))
    isPol(strToList(n))