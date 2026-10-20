def ReadData(file:str):
    f = open(file, 'r')
    n = int(f.readline())
    f.close()
    return n

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()
    return 'OK'

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\BinhPhuoc_(23-24)\\Bai1\\Test1.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\BinhPhuoc_(23-24)\\Bai1\\Test1.out'

n = ReadData(fIn)
tong = 0
for i in range(2,n,2):
    tong += i

print(WriteData(fOut, str(tong)))