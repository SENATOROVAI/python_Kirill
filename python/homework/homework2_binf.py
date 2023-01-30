'''\бинарный поиск... чего то...'''
from random import randint
a = []
for i in range(20):
    a.append(randint(1, 50))
a.sort()
print(a)
find_int = int(input())

# счетчик для себя
k = 0


mid = len(a) // 2
low = 0
high = len(a) - 1
 
while a[mid] != find_int and low <= high:
    if find_int > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
    k = k + 1
 
if low > high:
    print("No find", k)
else:
    print("int", mid, k)