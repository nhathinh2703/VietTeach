'''
Kiểm tra số tự nhiên n có phải là số đối xứng hay không?

Gợi ý: Để tìm số đảo ngược của một số có 2 cách:
- Duyệt xâu để tách kí tự
- Dùng phép chia tách số

B1. Nhập số n từ bàn phím.
B2. Tìm x là số đảo ngược của n.
B3. Thông báo: True nếu n == x ngược lại False

### CÁCH TÌM SỐ ĐẢO NGƯỢC
C1. Duyệt lùi
for i in range(len(n)-1, -1, -1):
    Lấy ra n[i] cộng thêm vào x

C2. Duyệt lùi
i = len(n)-1
while i >= 0:
    Lấy ra n[i] cộng thêm vào x
    i -= 1

C3. Duyệt tiến
for i in len(n):
    x = n[i] + x

C4. Dùng phép chia dư và nguyên để xử lí
ds = ''
while n>0:
    ds += str(n%10)
    n //= 10
# Kết quả ds sẽ chứa xâu đảo ngược của n
'''
def SoDaoNguoc(n:int):
    ds = []
    while n>0:
        ds.append(str(n % 10))
        n = n // 10
    return int(''.join(ds))

n = int(input('Nhập số nguyên n: '))
print(SoDaoNguoc(n))
#print(f'{n} là số đối xứng' if n == SoDaoNguoc(n) else f'{n} không là số đối xứng')