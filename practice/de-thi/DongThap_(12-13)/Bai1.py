def SoNguyenTo(n:int):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Nhập số nguyên n: '))
dsUoc, dsUocNT = [], []
for i in range(1,n+1):
    if n%i == 0:
        dsUoc.append(str(i))
        if SoNguyenTo(i):
            dsUocNT.append(str(i))
print(f'- Cac uoc la: {' '.join(dsUoc)}')
print(f'- Cac uoc nguyen to la: {' '.join(dsUocNT)}')