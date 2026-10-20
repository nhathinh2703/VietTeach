# ss = 1000

# Nhập số giây từ bàn phím
ss = int(input('Nhập số giây: '))
s = ss           # Lưu lại số giây ban đầu vào s để in kết quả

ngay = ss//86400 # Đổi giây sang ngày
ss = ss%86400    # Số giây còn lại sau khi đổi ngày

# Tương tự đổi giờ
gio = ss//3600   # Đổi giây sang giờ
ss = ss%3600     # Số giây còn lại sau khi đổi giờ

# Tương tự đổi phút
phut = ss//60    # Đổi giây sang phút
ss = ss%60       # Số giây còn lại sau khi đổi phút

# In kết quả
print(f'{s} giây = {ngay} ngày {gio} giờ {phut} phút {ss} giây')
