# 1. Đếm số lượng các phần tử lớn hơn 0
# 2. Đếm số lượng các phần tử nhỏ hơn hoặc bằng 0
# 3. Đếm số lượng các phần tử chẵn
# 4. Đếm số lượng các phần tử lẻ
# 5. Đếm số lượng các phần tử chia hết cho 3
# 6. Đếm số lượng các phần tử chia hết cho cả 2 và 3
# 7. Đếm số lượng các phần tử ở chỉ số chẵn

A = [4, 8, -3, 7, 9, 2, 0, 6, -4]

dem1 = 0
for i in range(len(A)):
    if A[i] > 0:
        dem1 += 1
print(f'1. Số lượng phần tử lớn hơn 0: {dem1}')

dem2 = 0
for i in range(len(A)):
    if A[i] <= 0:
        dem2 += 1
print(f'2. Số lượng phần tử nhỏ hơn hoặc bằng 0: {dem2}')