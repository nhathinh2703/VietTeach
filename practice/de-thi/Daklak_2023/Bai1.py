def Tong(n:int):
    kq = 0
    for i in range(1,n+1):
        kq += i
    return kq

# Nhập T và các số N
T = int(input('Nhập số T: '))
ds = []
for i in range(T):
    ds.append(int(input(f'Nhập test {i+1}: ')))

for i in ds:
    print(Tong(i))