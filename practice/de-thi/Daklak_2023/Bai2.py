def SoNguyenTo(n:int):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def SoDep(n:int):
    # Duyệt các chữ số của n, nếu chứa '3', '5', '7' thì return False
    for i in str(n):
        # if i == '3' or i == '5' or i == '7':
        #     return False
        if i in '357':
            return False
    return True

# CHƯƠNG TRÌNH CHÍNH
'''
B1. Nhập n từ bàn phím, gán đếm bằng 0
B2. Duyệt i từ 1 đến n:
    Nếu i là số nguyên tố:
        Nếu i là số đẹp:
            Tăng đếm
B3. In đếm
'''
n,dem = int(input('Nhập n: ')),0
for i in range(1,n+1):
    # Cách đếm 1
    # if SoNguyenTo(i) and SoDep(i):
    #     dem += 1

    # Cách đếm 2 (hiệu suất tốt hơn cách 1)
    if SoNguyenTo(i):
        if SoDep(i):
            dem += 1
print(dem)