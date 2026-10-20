'''
Viết chương trình nhập n số nguyên từ bàn phím. Hãy cho biết dãy số vừ nhập có bao nhiêu số nguyên tố và thông báo kết quả ra màn hình
Gợi ý:
B1. Nhập số nguyên n từ bàn phím, tạo danh sách ds và kq rỗng
B2. Lặp n lần:
        Thêm vào danh sách ds số nguyên nhập từ bàn phím
B3. Lặp i trong danh sách ds:
        Nếu i là số nguyên tố:
            Thêm vào danh sách kq
B4. In độ dài kq và kq là kết quả bài toán
'''
def SoNguyenTo(n:int):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def NhapDanhSach(n:int):
    ds = []
    for i in range(n):
        ds.append(int(input(f'nhập phần tử thứ {str(i+1)}: ')))
    return ds

n = int(input('nhập số n: '))
ds, kq = NhapDanhSach(n), []
for i in ds:
    if SoNguyenTo(i):
        kq.append(str(i))

print(f'Có {len(kq)} số nguyên tố')
print(f'Số nguyên tố đó là: {', '.join(kq)}')