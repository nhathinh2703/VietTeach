# In, tính tổng, đếm các số nguyên tố từ 1 đến n.
'''
B1. Nhập só nguyên n từ bàn phím, khởi tạo tong bằng 0 và ds bằng rỗng
B2. Lặp i từ 1 -> n
        Nếu i là số nguyên tố:
            Cộng thêm i vào tong
            Thêm i vào ds
            In (i, end = ' ')
B3. In tong
'''

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

n = int(input('Nhập số nguyên n: '))
tong = 0
ds = []

for i in range(1, n+1):
    if SoNguyenTo(i):
        tong += i
        ds.append(i)
        print(i, end=' ')

print(f'\nTổng các số nguyên số: {tong}')