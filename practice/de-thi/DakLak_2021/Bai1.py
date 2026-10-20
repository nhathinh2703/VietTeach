'''
B1. Nhập từ bàn phím số tiền, số gà, số vịt cách nhau bởi dấu cách, tách theo dấu cách lưu vào biến danh sách ds
B2. Gán các giá trị trong ds vào x, so_ga, so_vit
B3. Thử tất cả phương án:
Gán dem bằng 0 (biến dem dùng để đếm số phương án phù hợp)
Lặp gia_vit từ 1 đến x//so_vit:
    Lặp gia_ga từ (gia_vit+1) đến x//so_ga:
        Nếu gia_vit*so_vit + gia_ga*so_ga bằng x thì:
            Tăng đếm
            Có thể in gia_ga và gia_vit ra để xem và so sánh với đáp án
B4. In đáp án bài toán là số phương án phù hợp (dem)
'''

ds = input('Nhập số tiền, số gà, số vit: ').split()
soTien, soGa, soVit = int(ds[0]), int(ds[1]), int(ds[2])
dem = 0
for giaVit in range(1,soTien//soVit):
    for giaGa in range(giaVit+1,soTien//soGa):
        if giaGa*soGa+giaVit*soVit==soTien:
            dem += 1
            # print(f'Giá gà: {giaGa} và giá vịt: {giaVit}')
print(dem)