# 1. In ra các phần tử của danh sách
# 2. In ra các phần tử lớn hơn 0
# 3. In ra các phần tử nhỏ hơn hoặc bằng 0
# 4. In ra các phần tử chẵn
# 5. In ra các phần tử lẻ
# 6. In ra các phần tử chia hết cho 3
# 7. In ra các phần tử chia hết cho cả 2 và 3
# 8. In ra các phần tử ở chỉ số chẵn

A = [4, -6, -2, 9, 8, -1, 0]

print('*** Câu 1. In danh sách theo chỉ số (Cách 1)')
for i in range(len(A)):
    print(A[i], end=' ')

print('\n*** Câu 1. In danh sách theo phần tử (Cách 2)')
for i in A:
    print(i, end=' ')

print('\n*** Câu 2. In ra các phần tử lớn hơn 0')
for i in range(len(A)):
    if A[i] > 0:
        print(A[i], end=' ')

print('\n*** 3. In ra các phần tử nhỏ hơn hoặc bằng 0')
for i in range(len(A)):
    if A[i] <= 0:
        print(A[i], end=' ')

print('\n*** Câu 4. In ra các phần tử chẵn')
for i in range(len(A)):
    if A[i] % 2 == 0:
        print(A[i], end=' ')

print('\n*** Câu 5. In ra các phần tử lẻ')
for i in range(len(A)):
    if A[i] % 2 != 0:
        print(A[i], end=' ')

print('\n*** Câu 7. In ra các phần tử lẻ')
for i in range(len(A)):
    if A[i] % 2 == 0 and A[i] % 3 == 0:
        print(A[i], end=' ')

print('\n*** 8. In ra các phần tử ở chỉ số chẵn')
for i in range(len(A)):
    if i % 2 == 0:
        print(A[i], end=' ')