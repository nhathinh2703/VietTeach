# 1. Tính tổng các phần tử lớn hơn 0
# 2. Tính tổng các phần tử nhỏ hơn hoặc bằng 0
# 3. Tính tổng các phần tử chẵn
# 4. Tính tổng các phần tử lẻ
# 5. Tính tổng các phần tử chia hết cho 3
# 6. Tính tổng các phần tử chia hết cho cả 2 và 3
# 7. Tính tổng các phần tử ở chỉ số chẵn

A = [4, 8, -3, 7, 9, 2, 0, 6, -4]

tong1 = 0
for i in range(len(A)):
    if A[i] > 0:
        tong1 += A[i]
print(f'1. Tổng các phần tử lớn hơn 0: {tong1}')