''' TÌM XÂU ĐẢO NGƯỢC
CÁCH 1:
B1. Tạo xâu s bất kì, xâu kq rỗng
B2. Duyệt i theo xâu s:
        Gán cho kq bằng xâu i ghép với kq
B3. In ra kq
'''

# Cách 1 - Duyệt theo kí tự
s, kq = 'ba10', ''
for i in s:
    kq = i + kq
print('Cách 1 - Duyệt theo kí tự:', kq)

# Cách 2 - Duyệt theo vị trí
s, kq = 'ba10', ''
for i in range(len(s)):
    kq = s[i] + kq
print('Cách 2 - Duyệt theo vị trí:', kq)

# Cách 3 - Duyệt ngược theo vị trí
s, kq = 'ba10', ''
for i in range(len(s)-1,-1,-1):
    kq = kq + s[i]
print('Cách 3 - Duyệt ngược theo vị trí', kq)