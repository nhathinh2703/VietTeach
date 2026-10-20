# VD1: Truy cập phần tử trong mảng
# def get_element(arr:list, index:int):
#     value = arr[index]  # 1 thao tác -> o(1)
#     return value

# arr = [10, 20, 30, 40, 50, 25, -180]
# index = 2
# print(get_element(arr, index))

# VD2: Tính tổng các phần tử trong mảng array/list
# def find_max(arr:list):
#     Duyệt qua toàn bộ mảng để tìm max
#     max = arr[0]        # O(1)

#     for i in arr:       # O(n)
#         if i > max: 
#             max = i
#     return max          # O(1 + n) => O(n)

# print(find_max(arr))

# VD3: Tìm kiếm phần tử trong mảng array/list
def LinearSearch1(lst:list, x:int):
    for i in range(0,len(lst)):     # O(n)
        if lst[i] == x:
            return i
    return -1

arr = [10, 20, 30, 40, 50, 25, 180]
target = 180
print(LinearSearch1(arr, target))

# # VD3
# arr phải được sắp xếp trước khi áp dụng thuật toán tìm kiếm nhị phân
def binary_search(arr:list, target:int):
    # Mỗi lần chia đôi mảng
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

arrsorted = sorted(arr)
print(binary_search(arrsorted, target))

# VD4: Sắp xếp mảng array/list
def bubble_sort(arr):
    n = len(arr)                    # O(1)                               
    for i in range(n):              # O(n)
        for j in range(n-1):        # O(n)  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# O(n^2) là độ phức tạp thời gian của thuật toán sắp xếp nổi bọt (bubble sort) trong trường hợp xấu nhất.

# BT
def find_maxmin(arr:list):
    max = arr[0]        # O(1)
    for i in arr:       # O(n)
        if i > max: 
            max = i

    min = arr[0]        # O(1)
    for i in arr:       # O(n)
        if i < min: 
            min = i
    return max, min
# O(2n) => O(n)