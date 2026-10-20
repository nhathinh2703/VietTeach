'''
0 1 1 2 3 5 8 13 21 34 55 89 ...

B3. Tính tổng các số Fibonacci nhỏ hơn N

Ý tưởng: Lặp tìm số Fibonacci tiếp theo nhỏ hơn N cộng vào tong.

Thuật toán:
B1. Nhập số nguyên N từ bàn phím
B2. Gán F bằng [0,1] chính là 2 số Fibonacci đầu tiên
B3. Gán i bằng 2, gán tong bằng 1
B4. Trong khi (F[i-1] + F[i-2]) < N:
    Thêm vào F giá trị (F[i-1] + F[i-2])
    Cộng thêm vào tong giá trị (F[i-1] + F[i-2])
    Tăng i lên 1 đơn vị
B5. In tong ra màn hình

Input: Nhập N: 13
Output: Tổng: 20

Input: Nhập N: 30
Output: Tổng: 54
'''
N = int(input('Nhập số N: '))
F, i, tong = [0,1], 2, 1
while F[i-1] + F[i-2] < N:
    number = F[i-1] + F[i-2]
    F.append(number)
    tong += number
    i += 1
print(tong)
print(F)