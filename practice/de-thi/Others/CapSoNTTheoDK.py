'''
Đọc từ tệp *.inp để có số nguyên k
Bắt đầu từ i = 2
Danh sách ds = []
Trong khi True:
    Nếu i là số nguyên tố:
        Thêm i vào ds
        Nếu độ dài của ds >= 2:
            Nếu ds[len(ds)-1] - ds[len(ds)-2] >= k:
                In cặp số ds[len(ds)-1], ds[len(ds)-2]
                Dừng vòng lặp
    Tăng i lên 1 đơn vị
'''
def ReadData(file:str):
    f = open(file, 'r', encoding='utf-8')
    k = f.readline().strip()
    f.close()
    return k
def WriteData(file:str, content:str):
    f = open(file, 'w', encoding='utf-8')
    f.write(content)
    f.close()
def SoNguyenTo(n):
    if n<2: return False
    if n<4: return True
    for i in range(2,int(n**0.5)+2):
        if n%i==0:
            return False
    return True
fin='D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\NT.inp'
fout='D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\NT.out'
i=2
ds=[]
k = int(ReadData(fin))
while True:
    if SoNguyenTo(i):
        ds.append(i)
        if len(ds)>=2:
            if ds[len(ds)-1] - ds[len(ds)-2]>=k:
                print(ds[len(ds)-1], ds[len(ds)-2])
                break
    i+=1