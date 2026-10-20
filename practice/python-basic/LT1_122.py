'''
B1: Nhập xâu s từ bàn phím, tạo xâu kq rỗng
B2: Lặp i từ 0 đến 2:
        Cộng thêm vào xâu kq giá trị s[i]
B3: In xâu kq ra màn hình
'''

s, kq = input('Nhập xâu: '), ''
for i in range(3):
    kq = kq + s[i]
print(kq)