'''
B1: Nhập xâu s từ bàn phím
B2: Tạo kq = 'S không chứa chữ số nào'
B3: Lặp i từ 0 đến len(s)-1:
        Nếu '0' <= s[i] <= '9':
            Gán kq = 'S có chứa chữ số'
            Dừng vòng lặp (break)
B4: In ra kq
'''
s = input('Nhập xâu: ')
kq = 'S không chứa chữ số nào'
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        kq = 'S có chứa chữ số'
        break
print(kq)