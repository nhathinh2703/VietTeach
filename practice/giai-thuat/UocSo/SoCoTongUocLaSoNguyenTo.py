'''
Tìm số có tổng các ước của nó là một số nguyên tố trong đoạn [a,b].

B1. Định nghĩa hàm SoNguyenTo(n:int) -> bool (Đã viết hôm trước)
B2. Định nghĩa hàm TongUoc(n:int) -> Tổng các ước của số n

B3. Nhập các số nguyên a, b từ bàn phím; tạo ds = []
B4. Duyệt i từ a đến b:
        Tính x bằng tổng ước của số i
        Nếu x là số nguyên tố thì:
            i là số cần tìm -> Thêm i vào ds
B5. In ds
'''
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

def TongUoc(n:int):
    tong = 0
    for i in range(1,n+1):
        if n%i == 0:
            tong += i
    return tong

a, b, ds = int(input('Nhập số a: ')), int(input('Nhập số b: ')), []

for i in range(a,b+1):
    x = TongUoc(i)
    if SoNguyenTo(x):
        ds.append(i)
        
print(ds)