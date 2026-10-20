def ReadData(path:str):
    f = open(path, 'r')
    ds = f.readline().split()
    a, b, k = int(ds[0]), int(ds[1]), int(ds[2])
    f.close()
    return a, b, k

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()

fin = 'D:\\GitHub\\ezProgramming\\src\\Exams\\KhanhHoa_(23-24)\\DemGao\\demgao.inp'
fout ='D:\\GitHub\\ezProgramming\\src\\Exams\\KhanhHoa_(23-24)\\DemGao\\demgao.out'
a,b,k = ReadData(fin)
dem=0
for i in range(a,b+1):
    if i%k==0:
        dem+=1
WriteData(fout,str(dem))