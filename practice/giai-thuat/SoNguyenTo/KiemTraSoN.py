import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

'''
Kiểm tra số n có phải là số nguyên tố hay không.
B1. Nhập số nguyên n từ bàn phím. Tạo biến demUoc = 0
B2. Duyệt i từ 2 -> int(n//2):
        Nếu n chia hết cho i:
            Tăng demUoc 1 đơn vị
B3. 
'''

n = int(input('Nhập số nguyên n: '))
print(SoNguyenTo(n))