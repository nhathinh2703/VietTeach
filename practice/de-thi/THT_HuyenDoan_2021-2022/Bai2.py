a, b = int(input('Nhập a: ')), int(input('Nhập b: '))
thang = 0
lai = a*(0.8/100)
while a < b:
    thang += 1
    a += lai

print(thang)