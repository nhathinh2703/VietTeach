'''
Liệt kê, đếm, tính tổng các số hoàn hảo trong phạm vi [a,b].

B1. Nhập a, b nhập từ bàn phím và khởi tạo: ds, dem, tong = [], 0, 0

B2. Duyệt i từ a đến b:
    Nếu i là số hoàn hảo:
        Thêm i vào ds
        Tăng dem 1 đơn vị
        Cộng thêm vào tổng số i

B3. In ra ds, dem, tong
'''

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

a, b, ds, dem, tong = int(input('Nhập a: ')), int(input('Nhập b: ')), [], 0, 0

for i in range(a,b+1):
    if SoHoanHao(i):
        ds.append(i)
        dem += 1
        tong += i
        
print(f'Từ {a} đến {b}:')
print(f'Danh sách số hoàn hảo: {ds}')
print(f'Đếm các số hoàn hảo: {dem}')
print(f'Tổng các số hoàn hảo: {tong}')