# Viết chương trình nhập 100 số nguyên a, b, c, d từ bàn phím.
# Tìm số lớn nhất và số nhỏ nhất trong 3 số đó.

a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
c = int(input('Nhập số nguyên c: '))

max = a
if max < b:
    max = b
if max < c:
    max = c
    
min = a
if min > b:
    min = b
if min > c:
    min = c

print(f'Số lớn nhất: {max}')
print(f'Số nhỏ nhất: {min}')
