def SoDaoNguoc(n:int):
    ds = []
    while n>0:
        ds.append(str(n % 10))
        n = n // 10
    return int(''.join(ds))

def UCLN(a:int, b:int):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def ReadData(file:str):
    f = open(file, 'r')
    lst = f.readline().split()
    f.close()
    return int(lst[0]),int(lst[1])

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()

# CHƯƠNG TRÌNH CHÍNH
fIn = ''
fOut = ''
'''
a,b = ReadData(fIn)
'''