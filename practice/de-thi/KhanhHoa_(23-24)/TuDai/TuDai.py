def ReadDaTa(file:str):
    f = open(file, 'r')
    lst = [str(i) for i in f.readline().split()]
    f.close()
    return lst

def WriteDaTa(file:str, content:int):
    f = open(file,'w')
    f.write(str(content))
    f.close()

def TUDAI(lst):
    ds = []
    for i in range(0,len(lst)):
        if i + 1 != len(lst) - 1:
            if len(lst[0]) > len(lst[1]):
                lst[0] , lst[1] = lst[1] , lst[0]
    ds.append(lst[len(lst) -1])
    dodai = len(lst[len(lst) - 1])
    return ds,dodai

fin = 'D:\\GitHub\\ezProgramming\\src\\Exams\\KhanhHoa_(23-24)\\TuDai\\tudai.inp'
fout = 'D:\\GitHub\\ezProgramming\\src\\Exams\\KhanhHoa_(23-24)\\TuDai\\tudai.out'
lst = ReadDaTa(fin)

ds,dodai = TUDAI(lst)
print(dodai)
print(' '.join(map(str,ds)))
kq = f'{dodai}{'\n'}{' '.join(map(str,ds))}'
WriteDaTa(fout, kq)