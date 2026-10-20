# S = 1^3 + 2^3 + ... + n^3

# B1. Nhập số nguyên n từ bàn phím, gán S bằng 0
# B2. Tính tổng
# Lặp i từ 1 đến n:
#   Cộng thêm số i^3 vào S
# B3. In tổng ra màn hình

n, S = int(input('Nhập số tự nhiên n: ')), 0
for i in range(1,n+1):
    S += i**3
print(f'S = {S}')
