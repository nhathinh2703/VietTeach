def ReadDaTa(file:str):
    f = open(file,'r')
    lst = [str(i) for i in (str(f.readline()))]
    f.close()
    return lst
def WriteDaTa(file:str,content:int):
    f = open(file,'w')
    f.write(str(content))
    f.close()
def TimDsSo(lst):
    dsSo = []
    for i in lst:
        if '1' <= i <= '9':
            dsSo.append(int(i))
    return dsSo
def XapXep(ds1):
    ds = ds1
    for i in range(len(ds1)):
        for j in range(len(ds)-1):
            if ds[j] < ds[j+1]:
                ds[j] , ds[j+1] = ds[j+1] , ds[j]
    return ds
def DsCHuaSo(danh_sach):
    ds = []
    for i in range(3):
        ds.append(danh_sach[i])
    return ds
fin = 'D:\GitHub\\ezProgramming\\src\\Exams\\LaoCai_(25-26)\\Bai2\\test1.inp'
fout = 'D:\GitHub\\ezProgramming\\src\\Exams\\LaoCai_(25-26)\\Bai2\\test1.out'
lst = ReadDaTa(fin)
ds1 = TimDsSo(lst)
danh_sach = XapXep(ds1)
Number = ''.join(map(str, DsCHuaSo(danh_sach)))
print(Number)
WriteDaTa(fout, int(Number))