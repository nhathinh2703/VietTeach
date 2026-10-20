# Tìm các số nguyên tố có tổng chữ số cũng là số nguyên tố trong phạm vi từ [a,b]

'''
CHƯƠNG TRÌNH CON:
Định nghĩa hàm TongChuSo, đầu vào là số nguyên n, đầu ra là tổng các chữ số của số n
B1. Khởi tạo tong = 0
B2. Lặp i in xâu n:
        Chuyển kí tự i thành số nguyên và cộng thêm vào tong
B3. Trả về tong

CHƯƠNG TRÌNH CHÍNH:
B1. Nhập các số nguyên a, b từ bàn phím; Khởi tạo danh sách ds rỗng
B2. Lặp i từ a -> b:
        Nếu (i là số nguyên tố) và ((tổng chữ số của i) là số nguyên tố):
            Thêm số i vào danh sách ds
B3. In danh sách ds
'''
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

def TongChuSo(n:int):
    # tong = 0
    # for i in str(n):          # Duyệt xâu theo kí tự
    #     tong += int(i)
    # return tong

    tong = 0
    s = str(n)
    for i in range(len(s)):     # Duyệt xâu theo vị trí
        tong += int(s[i])
    return tong

a, b, ds = int(input('Nhập số nguyên a: ')), int(input('Nhập số nguyên b: ')), []
for i in range(a, b+1):
    if SoNguyenTo(i) and SoNguyenTo(TongChuSo(i)):
        ds.append(i)
print(ds)