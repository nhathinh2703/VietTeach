def ReadData(file:str):
    f = open(file, 'r')
    n = int(f.readline())
    ds = f.readline().split()
    f.close()
    return n,ds

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()
    print('OK!')

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DongThap_(12-13)\\Bai3\\Test1.inp'
fCan = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DongThap_(12-13)\\Bai3\\Can1.out'
fHuy = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DongThap_(12-13)\\Bai3\\Huy1.out'

n,ds = ReadData(fIn)
tong, dsHuy = 0, []

for i in range(len(ds)):
    tong += int(ds[i])
    if int(ds[i]) > 20:
        dsHuy.append(str(i+1))

WriteData(fCan, str(tong))
WriteData(fHuy, '\n'.join(dsHuy))