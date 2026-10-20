def SoNguyenTo(n:int):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def TongBinhPhuongC1(n:int):
    tong = 0
    for i in str(n):
        tong += int(i)**2
    return tong

def TongBinhPhuongC2(n:int):
    tong = 0
    while n > 0:
        du = n%10
        n = n//10
        tong += du**2
    return tong