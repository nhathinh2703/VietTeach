def TatCaGiongNhau(a:str):
    first = a[0]
    for i in a:
        if i != first:
            return False
    return True

N = int(input('Nhập số N: '))
dem = 0
for i in range(18,N,9):
    if TatCaGiongNhau(str(i)):
        dem += 1
print(dem)