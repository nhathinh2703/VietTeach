def ReadDaTa(file:str):
    f = open(file, 'r', encoding='utf-8')
    lst = f.readline()
    lst2 = f.readline()
    f.close()
    return lst,lst2
def WriteDaTa(file:str, content:str):
    f = open(file, 'w', encoding='utf-8')
    f.write(content)
    f.close()
def xuly(lst:str,lst1,lst2):
    ds = []
    count = 0
    for i in range(0,len(lst1)):
        if lst2 == lst1[i]:
            count += 1
            ds.append(i+1)
    if count > 0:
        kq = f'xâu {lst2} xuất hiện {count} lần trong xâu {lst.strip()} và vị trí đầu tiên xuất hiện là vị trí số: {ds[0]}'
        return kq
    if count < 0:
        return 'không xuất hiện xâu'
fin = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\Bai2TimXau.inp'
fout = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\Bai2TimXau.out'
lst,lst2 = ReadDaTa(fin)
lst1 = []
n = len(lst2)
for i in range(0, len(lst)+1 , n):
    lst1.append(lst[i:i+n])
kq = xuly(lst,lst1,lst2)
print(kq)
WriteDaTa(fout, str(kq))