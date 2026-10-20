def ReadData(file:str):
    f = open(file, 'r')
    ds = f.readline().split()
    f.close()
    return int(ds[0]), int(ds[1])

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()
    return 'OK'

def TongUocThucSu(n:int):
    tong = 0
    for i in range(1,n):
        if n%i == 0:
            tong += i
    return tong


fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\BinhPhuoc_(23-24)\\Bai3\\Test4.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\BinhPhuoc_(23-24)\\Bai3\\Test1.out'

a,b = ReadData(fIn)
ds = []
for i in range(a, b+1):
    if TongUocThucSu(i) > i:
        ds.append(i)

print(ds)
print(len(ds))