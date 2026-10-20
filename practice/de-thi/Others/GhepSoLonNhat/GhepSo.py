def ReadData(file:str):
    f = open(file, 'r')
    n = int(f.readline())
    ds = f.readline().split()
    f.close()
    return n, ds

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\GhepSoLonNhat\\Test2.inp'
fout = 'D:\\GitHub\\ezProgramming\\src\\Exams\\Others\\GhepSoLonNhat\\Test2.out'

n, ds = ReadData(fIn)

# Sắp xếp ds giảm dần
ds.sort(reverse=True)
result = ''.join(ds)
print(result)
WriteData(fout, result)