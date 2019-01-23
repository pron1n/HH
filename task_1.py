def xString(n):
    seq = []
    pos = []
    for i in range(len(n) - 1):
        s = 0
        for j in range(len(n) - i):
            s += int(n[i + j])
            if s == 10:
                seq.append(n[i:(i + j + 1)])
                pos.append(i)
    xS = ["x" for x in range(len(n))]
    k = 0
    for i in pos:
        for j in range(len(seq[k])):
             xS[i + j] = seq[k][j]
        k += 1
    return "".join(xS)

#c = 0
#for i in range(10, 1900001):
#    if xString(str(i)) == str(i):
#        c += 1
#print(c)

while True:
    n = input("Число: ")
    if xString(str(n)) == str(n):
        print("Wonder!")
    else:
        print("no:(")