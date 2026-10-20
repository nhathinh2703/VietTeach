# HÀM CÓ SẴN TRONG PYTHON
num = 25
print(bin(num))     # Chuyển số num ở hệ 10 sang hệ 2 -> KQ: 0b11001
print(oct(num))     # Chuyển số num ở hệ 10 sang hệ 8 -> KQ: 0o31
print(hex(num))     # Chuyển số num ở hệ 10 sang hệ 16 -> KQ: 0x19
print(hex(200))     # Chuyển số 200 ở hệ 10 sang hệ 16 -> KQ: 0xc8

print(format(num,'b'))  # Biểu diễn số num ở hệ 2 ('b': binary) > KQ: 11001
print(format(num,'o'))  # Biểu diễn số num ở hệ 8 ('o': octal) > KQ: 31
print(format(num,'X'))  # Biểu diễn số num ở hệ 16 ('X': hex) > KQ: 19
print(format(200,'X'))  # Biểu diễn số num ở hệ 16 ('X': hex) > KQ: C8
print(format(200,'x'))  # Biểu diễn số num ở hệ 16 ('x': hex) > KQ: c8