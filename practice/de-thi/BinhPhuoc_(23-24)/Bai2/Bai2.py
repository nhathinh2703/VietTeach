def ReadData(file:str):
    f = open(file, 'r')
    ds = f.readline().split()
    f.close()
    return int(ds[0]), int(ds[1]), int(ds[2])

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()
    return 'OK'
fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\BinhPhuoc_(23-24)\\Bai2\\Test3.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\BinhPhuoc_(23-24)\\Bai2\\Test1.out'

t, a, b = ReadData(fIn)
tien = 0
if t==1 or t==7:
    # Tính tiền theo ngày lễ
    for i in range(a+1,b+1):
        if i <= 12:
            tien += 10
        elif i <= 18:
            tien += 15
        else:
            tien += 20  
else:
    # Tính tiền theo ngày thường
    for i in range(a+1,b+1):
        if i <= 12:
            tien += 6
        elif i <= 18:
            tien += 10
        else:
            tien += 20

print(tien) 