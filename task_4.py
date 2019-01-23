size = input("SIZE: ")

cornerLeft = size ** 2 - (size - 1)

digSum1 = 1
cur = 1
diff = 0
while cur < cornerLeft:
    diff += 2
    cur += diff
    digSum1 += cur

digSum2 = 1
cur = 1
diff = 0
while cur < size ** 2:
    diff += 4
    cur += diff
    digSum2 += cur
    cur += diff
    digSum2 += cur

print(digSum1 + digSum2 - 1)