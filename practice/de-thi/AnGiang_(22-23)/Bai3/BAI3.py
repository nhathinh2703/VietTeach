# Đọc dữ liệu từ tệp: Mở để đọc -> Đọc -> Đóng
def ReadData(file:str):
    f = open(file, 'r')         # B1. Mở để đọc
    ds = f.readline().split()   # B2. Đọc 1 dòng và xử lí
    s = f.readline()            # B2. Đọc 1 dòng tiếp theo
    f.close()                   # B3. Đóng tệp
    return int(ds[0]), ds[1], s

# Ghi dữ liệu vào tệp: Mở để ghi -> Ghi -> Đóng
def WriteData(file:str, content:str):
    f = open(file, 'w')         # B1. Mở để ghi
    f.write(content)            # B2. Ghi danh sách vào tệp
    f.close()                   # B3. Đóng tệp

def TachXau(s:str,n:int):
    ds = []
    # Xử lí tách xâu
    for i in range(0,len(s),n):
        group = s[i:i+n]
        # while len(group) < 8:
        #     group += ' '
        if len(group) < 8:
            group += (n-len(group))*' '
        ds.append(group)
    return ds

def MaHoa(ds:list,key:str):
    kq = []
    # Mã hóa ds
    for nhom in ds:
        # Lấy ra được từng nhóm -> Sắp xếp theo key
        s = ''
        for j in key:
            s += nhom[int(j)-1]
        kq.append(s)
    return kq

# CHƯƠNG TRÌNH CHÍNH
fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\AnGiang_(22-23)\\Bai3\\TEST1.INP'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\AnGiang_(22-23)\\Bai3\\TEST1.OUT'

n,key,s = ReadData(fIn)
ds = TachXau(s,n)
kq = MaHoa(ds,key)
WriteData(fOut,'\n'.join(kq))
print('OK!')