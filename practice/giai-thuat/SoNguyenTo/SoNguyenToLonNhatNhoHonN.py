# Tìm số nguyên tố lớn nhất nhỏ hơn n.
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from __utils__ import *

# Cách 1: Duyệt từ 2 đến (n-1) để tìm số nguyên tố gần n nhất
n = int(input("Nhập n: "))
ds = []
for i in range(2, n):
    if SoNguyenTo(i):
        ds.append(i)
if len(ds) > 0:
    print(ds[len(ds) - 1])
else:
    print(-1)
'''
# Tìm số nguyên tố lớn nhất nhỏ hơn n.
Cách 2: Duyệt ngược từ (n-1) về 2 để tìm số nguyên tố gần n nhất.
n = int(input("Nhập n: "))
i = n-1
soCanTim = -1
while i >= 2:
    if SoNguyenTo(i):
        soCanTim = i
        break
    i -= 1
print(soCanTim)
'''