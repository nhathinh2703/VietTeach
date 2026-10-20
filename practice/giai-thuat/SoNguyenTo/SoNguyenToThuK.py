'''
# Tìm số nguyên tố thứ k.

Bước 1: Nhập số nguyên k từ bàn phím, khởi tạo i = 2, dem = 0
Bước 2: Trong khi True:
              if SoNguyenTo(i):
                  Tăng dem thêm 1 đơn vị
                  Nếu dem == k:
                      In số i
                      Dừng vòng lặp
              Tăng i thêm 1 đơn vị
'''
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

k,i,dem = int(input('Nhập số nguyên k: ')),2,0
while True:
    if SoNguyenTo(i):
        dem += 1
        if dem == k:
            print(i)
            break
    i += 1