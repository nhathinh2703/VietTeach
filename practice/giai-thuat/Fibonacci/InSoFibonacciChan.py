'''
Tìm số Fibonacci chẵn trong đoạn [a,b]

Thuật toán:
B1. Nhập số nguyên a, b từ bàn phím. Gán F bằng [0,1], gán i bằng 2, gán R bằng [], dem bằng 0
B2. Trong khi (F[i-1] + F[i-2]) <= b:
        num = F[i-1] + F[i-2]
        Thêm num vào trong danh sách F
        Nếu num >= a:
            Thêm num vào R
            dem += 1
        Tăng i lên 1 đơn vị
B3. Duyệt i trong danh sách R:
        Nếu i là số chẵn:
            In i
'''
import time
start = time.perf_counter()
a, b = int(input('Nhập số a: ')), int(input('Nhập số b: '))
F, R, i, dem = [0,1], [], 2, 0
while F[i-1] + F[i-2] <= b:
    num = F[i-1] + F[i-2]
    F.append(num)
    if num >= a:
        R.append(num)
        dem += 1
    i += 1
    
print(F)
print(R)
for i in R:
    if i%2==0:
        print(i, end=' ')
print(f'{'\n'}{dem}')
end = time.perf_counter()
print(f'Thời gian thực hiện: {end-start}')