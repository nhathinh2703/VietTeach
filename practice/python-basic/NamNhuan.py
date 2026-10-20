# Viết chương trình kiểm tra năm m nhập từ bàn phím
# có phải là năm nhuận hay không.

# Bước 1: Nhập năm m (số nguyên) từ bàn phím.
# Bước 2:
# Nếu (m chia hết cho 400) hoặc (m chia hết cho 4 và m không chia hết cho 100) thì:
#   Thông báo m là năm nhuận
# Ngược lại:
#   Thông báo m không là năm nhuận

m = int(input('Nhập năm dương lịch: '))
if (m%400==0) or (m%4==0 and m%100!=0):
    print(f'Năm {m} là năm nhuận, số ngày: 366')
else:
    print(f'Năm {m} không là năm nhuận, số ngày: 365')


