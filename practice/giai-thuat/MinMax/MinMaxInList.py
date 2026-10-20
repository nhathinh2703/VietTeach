# CHƯƠNG TRÌNH CON
def MinIndex(lst:list):
    minIndex = 0
    for i in range(1,len(lst)):
        if lst[i] < lst[minIndex]:
            minIndex = i
    return minIndex

# CHƯƠNG TRÌNH CHÍNH
lst = [5, 9, 0, 1, 7, 4, 8, 10]
minIndex = MinIndex(lst)
print(f'Phần tử nhỏ nhất là: {lst[minIndex]} ở vị trí: {minIndex}')