# Viết chương trình tính tổng S:
# S = 1+2+3+......+10

# Cách 1: Tính tổng trực tiếp
print(f'Cách 1: S = {1+2+3+4+5+6+7+8+9+10}')

# Cách 2: Sử dụng vòng lặp
S = 0
for i in range(1,11):
    S = S + i
print(f'Cách 2: S = {S}')

# Viết chương trình tính tổng T:
# T = 1+2+3+......+n, với n là số nguyên nhập từ bàn phím
n = int(input('Nhập số nguyên N: '))
T = 0
for i in range(1,n+1):
    T += i
print(f'T = {T}')

# Viết chương trình tính U:
# U = 1 x 2 x 3 x ...... x K, với K là số nguyên nhập từ bàn phím
k = int(input('Nhập số nguyên k: '))
U = 1
for i in range(1,k+1):
    U = U*i
print(U)

