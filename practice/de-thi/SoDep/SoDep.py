# import TienIch
# import TienIch as t
from TienIch import *
# from TienIch import SoNguyenTo, TongBinhPhuongC1

# CHƯƠNG TRÌNH CHÍNH
n = int(input('Nhập n: '))
dem = 0
so = 0
ds = []
while dem < n:
    so += 1
    if SoNguyenTo(TongBinhPhuongC1(so)):
        dem += 1
        ds.append(so)
print(so) 
print(ds)