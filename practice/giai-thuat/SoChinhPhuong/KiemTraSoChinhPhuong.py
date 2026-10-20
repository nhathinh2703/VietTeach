'''
Kiểm tra số N có phải là SCP hay không?

B1. Tính x là phần nguyên (căn bậc 2 của n).
B2. So sánh: x**2 == n (Kết quả True/False là SCP/không là SCP)

Có thể định nghĩa hàm dùng chung: SoChinhPhuong(n:int) -> True/False
'''

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

n = int(input('Nhập số n: '))
print(SoChinhPhuong(n))