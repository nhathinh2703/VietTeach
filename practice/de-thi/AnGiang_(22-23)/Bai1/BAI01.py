def ReadData(path:str):
    f = open(path, 'r')
    lst = f.readline().split()  
    f.close()
    return int(lst[0]), int(lst[1]), int(lst[2])

def WriteData(path:str, content:str):
    f = open(path, 'w')
    f.write(content)
    f.close()

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\AnGiang_(22-23)\\Bai1\\BAI01.INP'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\AnGiang_(22-23)\\Bai1\\BAI01.OUT'
a,b,c = ReadData(fIn)
result = (a**b)%c
WriteData(fOut, str(result))
print('OK')