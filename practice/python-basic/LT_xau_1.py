'''
Input: '3 9 6 2 4'
Output: 24

B1. Nhập xâu s từ bàn phím, tạo biến tong bằng 0
B2. Tách xâu s theo dấu cách gán vào danh sách A
B3. Lặp i theo A:
        Cộng thêm vào tong số nguyên/thực i
B4. In tong ra màn hình
'''

s, tong = input('Nhập xâu: '), 0
A = s.split()
for i in A:
    tong += float(i)
print(tong)