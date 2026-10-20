'''
BÀI TOÁN: Tìm UCLN và BCNN của hai số tự nhiên a và b

CÁCH 1: Duyệt từ số nhỏ nhất về 1, nếu cả a và b chia hết cho số nào đầu tiên thì số đó là UCLN.
B1. Nhập số nguyên a và b từ bàn phím
B2. Tìm x = min(a,b), ucln = -1
B3. Duyệt i từ x về 1:
        Nếu cả a và b đều chia hết cho i:
            i là UCLN -> Gán i vào biến ucln
            Dừng vòng lặp
B4. bcnn = (a*b)/ucln
B5. In ucln và bcnn

CÁCH 2: Thuật toán Euclid (phép trừ):
Ý tưởng: Nếu a>b thì UCLN(a,b) = UCLN(a-b,b).
Ngược lại nếu a<b UCLN(a,b) = UCLN(a,b-a).
Lặp lại cho đến khi a=b, khi đó UCLN=a hoặc UCLN=b.

B1. Trong khi a != b:
        Nếu a>b: a = a-b
        Ngược lại: b = b-a
B2. ucln = a hoặc ucln = b

CÁCH 3: Thuật toán Euclid (phép chia)
Ý tưởng: UCLN(a,b) = UCLN(b,a%b). Lặp lại cho đến khi số dư bằng 0. Khi đó, số còn lại chính là UCLN.

B1. Trong khi b != 0:
        r = a%b
        a = b
        b = r
B2. ucln = a
'''

def UCLN_C1(a:int, b:int):
    i, ucln = min(a,b), -1
    while i >= 1:
        if a%i==0 and b%i==0:
            ucln = i
            break
        i -= 1
    return ucln

def UCLN_C2(a:int, b:int):
    while a != b:
        if a>b: a = a-b
        else: b = b-a
    return a

def UCLN_C3(a:int, b:int):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

a,b = int(input('Nhập số a: ')), int(input('Nhập số b: '))
print('C1:', UCLN_C1(a,b))
print('C2:', UCLN_C2(a,b))
print('C3:', UCLN_C3(a,b))