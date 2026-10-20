# B1. Nhập cân nặng (cn) từ bàn phím
# B2. Nhập chiều cao (cc) từ bàn phím
# B3. Tính và in ra chỉ số bmi = cn/(cc**2)
# B4. Dùng câu lệnh rẽ nhánh để thông báo kết luận
# Nếu bmi < 18.5 thì
#   Thông báo "Thiếu cân"
# Nếu bmi >= 18.5 và bmi <= 22.9 thì
#   Thông báo "Bình thường"
# Nếu bmi >= 23 thì
#   Thông báo "Thừa cân"

cn = float(input('Nhập cân nặng (ki-lô-gam): '))
cc = float(input('Nhập chiều cao (mét): '))
bmi = round(cn/(cc**2),1)   # Làm tròn 1 số thập phân sau dấu chấm
print(f'Chỉ số BMI của bạn: {bmi}')
if bmi < 18.5:
    print('Bạn đang thiếu cân')
if 18.5 <= bmi <= 22.9:
    print('Bình thường')
if bmi >= 23:
    print('Bạn đang thừa cân')
