import time


inp_str = input("Строка: ")

start_time = time.time()

list_num = inp_str.split(" ")


for i in range(1, 1000001):
    if str(i) not in list_num:
        print(i)
        break


list_num.sort()
print(list_num)
print(len(list_num))


print("\ntime, sec:", time.time() - start_time)

