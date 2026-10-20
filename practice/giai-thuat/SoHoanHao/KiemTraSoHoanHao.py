'''
Kiểm tra số nguyên dương n có phải là số hoàn hảo hay không?

B1. Nhập số nguyên dương n từ bàn phím, khởi tạo biến tong bằng 0
B2. Duyệt i từ 1 đến (n-1):
        Nếu n chia hết cho i:
            Cộng thêm i vào tong
B3. Nếu tong bằng số n thì:
        Thông báo True
    Ngược lại:
        Thông báo False

Có thể định nghĩa hàm dùng chung: SoHoanHao(n:int) -> True/False
'''

n, tong = int(input('Nhập số nguyên n: ')), 0
for i in range(1,n):
    if n%i == 0:
        tong += i
# if tong == n:
#     print(f'{n} là số hoàn hảo')
# else:
#     print(f'{n} không là số hoàn hảo')

# print(tong == n)

# <giá trị nếu đúng> if <điều kiện> else <giá trị nếu sai>
print(f'{n} là số hoàn hảo' if tong == n else f'{n} không là số hoàn hảo')