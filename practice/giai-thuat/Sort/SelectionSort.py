def SelectionSort(lst:list, ascending:bool):
    for i in range(len(lst)-1):
        index = i
        for j in range(i+1,len(lst)):
            if ascending:
                if lst[j] < lst[index]:
                    index = j
            else:
                if lst[j] > lst[index]:
                    index = j
        lst[i],lst[index] = lst[index],lst[i]
    
    return lst

A = [12, 15, 8, 3, 5, 7, -5, -20, 7, 1]
print(SelectionSort(lst=A, ascending=False))