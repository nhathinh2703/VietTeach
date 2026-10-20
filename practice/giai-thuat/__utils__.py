def SoNguyenTo(n:int):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def SoHoanHao(x:int):
    tong = 0
    for i in range(1,x):
        if x%i == 0:
            tong += i
    return tong == x

def SoChinhPhuong(n:int):
    x = int(n**0.5)
    return x*x == n