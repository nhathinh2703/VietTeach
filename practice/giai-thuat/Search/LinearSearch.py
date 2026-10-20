import random
from datetime import datetime

def LinearSearch1(lst:list, x:int):
    for i in range(0,len(lst)):
        if lst[i] == x:
            return i
    
    return -1

def LinearSearch2(lst:list, x:int):
    i = 0
    while i < len(lst):
        if lst[i] == x:
            return i
        i += 1
    
    return -1

def BinarySearch(lst:list, x:int):
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def CreateListRandom(n:int):
    lst = []
    for i in range(n):
        lst.append(random.randint(-300, 300))
    return lst

def LinearSearch3(lst:list, x:int):
    result = []
    for i in range(0,len(lst)):
        if lst[i] == x:
            result.append(i)
    return result

lst = CreateListRandom(10000000)
x = 100
print(lst)

start = datetime.now()
result = LinearSearch3(lst, x)
end = datetime.now()

startBinary = datetime.now()
resultBinary = BinarySearch(lst, x)
endBinary = datetime.now()

print(result)
print(start)
print(end)
print(end-start)

print(resultBinary)
print(startBinary)
print(endBinary)
print(endBinary-startBinary)