def ReadData(file:str):
    f = open(file, 'r')
    number = int(f.readline())
    f.close()
    return number

def WriteData(file:str, content:str):
    f = open(file, 'w')
    f.write(content)
    f.close()

def CheckNumber(m:int):
    for i in str(m):
        if i != '1' and i != '0':
            return False
    return True

def Process(n:int):
    i = 1
    while not CheckNumber(n*i):
        i += 1
    return n*i

fIn = 'D:\\GitHub\\ezProgramming\\src\\Exams\\AnGiang_(22-23)\\Bai4\\TEST2.INP'
fOut = 'D:\\GitHub\\ezProgramming\\src\\Exams\\AnGiang_(22-23)\\Bai4\\TEST2.OUT'

n = ReadData(fIn)
m = Process(n)
WriteData(fOut, str(m))
print('OK')