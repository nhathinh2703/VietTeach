'''
B1. Nhập chuỗi số (s), cơ số (b), ketQua = 0, số mũ n = len(s) - 1, 
chuyen = '0123456789ABCDEF'
B2. Lặp i từ 0 đến len(s)-1:
        Cộng thêm vào ketQua giá trị: chuyen.index(s[i]) * b**n
        Giảm n 1 đơn vị
B3. In ketQua
'''
def ChuyenDoi(chuoi_so:str, co_so:int):
    ketQua, n, chuyen = 0, len(chuoi_so) - 1, '0123456789ABCDEF'
    for i in range(len(chuoi_so)):
        ketQua += chuyen.index(chuoi_so[i]) * co_so**n
        n -= 1
    return ketQua

print(ChuyenDoi('11101',2))
print(ChuyenDoi('31',8))
print(ChuyenDoi('C8',16))
print('------------')

# HÀM CÓ SẴN TRONG PYTHON
print(int('11101',2))   # Chuyển '11101' ở hệ 2 sang hệ 10 -> KQ: 25
print(int('31',8))      # Chuyển '31' ở hệ 8 sang hệ 10 -> KQ: 25
print(int('C8',16))     # Chuyển 'C8' ở hệ 16 sang hệ 10 -> KQ: 200