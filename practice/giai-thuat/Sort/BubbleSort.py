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

lst = [12, 15, 8, 3, 5, 7]
lstAsc = BubbleSort(lst.copy(),True)
print(lst)
print(lstAsc)