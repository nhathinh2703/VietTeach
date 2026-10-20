# Tìm tất cả cặp số nguyên tố sinh đôi trong đoạn [a, b].

'''
B1. Nhập các số nguyên a, b từ bàn phím, khởi tạo danh sách ds rỗng.
B2. Lặp i từ a -> (b-2):
        Nếu i và (i+2) đều là nguyên tố:
            Thêm cặp (i,i+2) vào ds
B3. In ds ra màn hình
'''
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

a, b, ds = int(input('Nhập số nguyên a: ')), int(input('Nhập số nguyên b: ')), []
for i in range(a, b-1):
    if SoNguyenTo(i) and SoNguyenTo(i+2):
        ds.append(f"({i},{i+2})")
print('; '.join(ds))