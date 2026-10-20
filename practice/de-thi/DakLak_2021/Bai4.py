def BubbleSort(lst:list, ascending:bool):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if ascending:
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                if lst[j] < lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

n = int(input('Nhập số N: '))
s = input(f'Nhập danh sách {n} số: ')
lst = [int(i) for i in s.split()]
lst = BubbleSort(lst,False)
kq = lst[0]*lst[1]*lst[2]
print(kq)

''' Cách 1
lst = []
for i in s.split():
    lst.append(int(i))
'''

'''Cách 2
lst = [int(i) for i in s.split()]
'''
# map(hàm,dãy): Áp dụng "hàm" lên từng phần tử của "dãy" và trả về đối tượng map
'''Cách 3
lst = list(map(int,s.split()))
'''