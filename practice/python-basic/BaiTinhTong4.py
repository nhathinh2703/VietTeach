# S = 1 + 3 + 5 + ... + (2n-1)
# với n là số tự nhiên nhập từ bàn phím
n, S = int(input('Nhập số tự nhiên n: ')), 0
for i in range(1, 2*n, 2):
    S += i
print(f'S = {S}')

# BTVN 1:
# T = 2 + 4 + 6 + ... + 2n
# với n là số tự nhiên nhập từ bàn phím

# BTVN 2:
# U = 2 + 4 + 6 + ... + 2n + 2025
# với n là số tự nhiên nhập từ bàn phím
