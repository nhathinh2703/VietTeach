'''
Nhập n là số tự nhiên từ bàn phím. Từ 1 đến n:
1. In ra màn hình các số chia hết cho 3.
2. Đếm số lượng các số chia hết cho 3 và 5.

Gợi ý:
Bước 1: Nhập số tự nhiên n từ bàn phím
Bước 2: Gán count bằng 0
Bước 3:
Lặp i từ 1 đến n:
    Nếu i chia hết cho 3 thì:
        In số i ra màn hình

    Nếu (i chia hết cho 3) và (i chia hết cho 5) thì:
        Tăng count thêm 1 đơn vị

B4. In count ra màn hình
'''
n = int(input('Nhập số tự nhiên n: '))
count = 0
for i in range(1,n+1):
    if i%3==0:
        print(i,end=' ')

    if i%3==0 and i%5==0:
        count += 1

print()
print(count)

    
    
