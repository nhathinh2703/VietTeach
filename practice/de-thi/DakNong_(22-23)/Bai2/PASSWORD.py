def SoNguyenTo(n:int):
    if n < 2: return False
    if n < 4: return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def TongChuSo(n:int):
    tong = 0
    for i in str(n):
        tong += int(i)
    return tong

# Viết hàm ReadData(file:str) đọc l, r từ file
def ReadData(file:str):
    f = open(file, 'r')
    ds = f.readline().split()
    f.close()
    return int(ds[0]), int(ds[1])

# Viết hàm WriteData(file:str, content:str) ghi content vào file
def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()

# CHƯƠNG TRÌNH CHÍNH
fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DakNong_(22-23)\\Bai2\\PASSWORD.INP'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DakNong_(22-23)\\Bai2\\PASSWORD.OUT'
l,r = ReadData(fIn)
ds = []
for i in range(l,r+1):
    if SoNguyenTo(i):
        if SoNguyenTo(TongChuSo(i)):
            ds.append(str(i))
content = ' '.join(ds)
WriteData(fOut, content)
print('OK')

'''
fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DakNong_(22-23)\\Bai2\\PASSWORD.INP'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DakNong_(22-23)\\Bai2\\PASSWORD.OUT'

B1. Gán l,r = ReadData(...)
    Gán ds = []
B2. Duyệt i từ l đến r:
        Nếu i là số nguyên tố:
            Nếu tổng chữ số của i là số nguyên tố:
                Chuyển i thành xâu và thêm vào ds
B3. Tạo xâu content từ danh sách ds (dùng join để nối)
    Dùng hàm WriteData để ghi content
'''