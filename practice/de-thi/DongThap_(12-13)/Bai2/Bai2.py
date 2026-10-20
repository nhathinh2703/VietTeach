def ReadData(file:str):
    f = open(file, 'r')
    line = f.readline()
    f.close()
    return line

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()
    print('OK!')

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DongThap_(12-13)\\Bai2\\Test6.inp'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\DongThap_(12-13)\\Bai2\\Test6.out'

s = ReadData(fIn)
p = 0
for i in s:
    if '0'<=i<='9':
        p += int(i)
WriteData(fOut,str(p))